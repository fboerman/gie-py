import requests
import pandas as pd
from typing import List, Dict, Union
from .agsi_mappings import AGSICompany, AGSIStorage, AGSICountry, lookup_company, lookup_storage, lookup_country
from .alsi_mappings import ALSITerminal, ALSILSO, ALSICountry, lookup_terminal, lookup_lso, lookup_country as lookup_country_alsi
from .exceptions import *
from enum import Enum

__title__ = "gie-py"
__version__ = "0.4.3"
__author__ = "Frank Boerman"
__license__ = "MIT"


class APIType(str, Enum):
    AGSI = "https://agsi.gie.eu/api"
    ALSI = "https://alsi.gie.eu/api"


class GieRawClient:
    def __init__(self, api_key):
        self.s = requests.Session()
        self.s.headers.update({
            'user-agent': f'gie-py v{__version__} (github.com/fboerman/gie-py)',
            'x-key': api_key
        })

    def _fetch(self, obj, t: APIType,
               start: Union[pd.Timestamp, str], end: Union[pd.Timestamp, str]):
        if type(start) != pd.Timestamp:
            start = pd.Timestamp(start)
        if type(end) != pd.Timestamp:
            end = pd.Timestamp(end)

        def _fetch_one(start, end, obj, page=1):
            r = self.s.get(t.value, params={
                'from': start.strftime('%Y-%m-%d'),
                'till': end.strftime('%Y-%m-%d'),
                'size': 300,
                'page': page
            } | obj.get_params())
            r.raise_for_status()

            return r.json()

        r = _fetch_one(start, end, obj)
        data = r['data']
        if r['last_page'] != 1:
            for p in range(2, r['last_page'] + 1):
                data += _fetch_one(start, end, obj, page=p)['data']

        if len(data) == 0:
            raise NoMatchingDataError

        return data

    def query_gas_storage(self, storage: Union[AGSIStorage, str],
                          start: Union[pd.Timestamp, str], end: Union[pd.Timestamp, str]) -> List[Dict]:
        storage = lookup_storage(storage)
        return self._fetch(storage, APIType.AGSI, start=start, end=end)

    def query_gas_company(self, company: Union[AGSICompany, str],
                          start: Union[pd.Timestamp, str], end: Union[pd.Timestamp, str]) -> List[Dict]:
        company = lookup_company(company)
        return self._fetch(company, APIType.AGSI, start=start, end=end)

    def query_gas_country(self, country: Union[AGSICountry, str],
                      start: Union[pd.Timestamp, str], end: Union[pd.Timestamp, str]) -> List[Dict]:
        country = lookup_country(country)
        return self._fetch(country, APIType.AGSI, start=start, end=end)

    def query_lng_terminal(self, terminal: Union[ALSITerminal, str],
                           start: Union[pd.Timestamp, str], end: Union[pd.Timestamp, str]) -> List[Dict]:
        terminal = lookup_terminal(terminal)
        return self._fetch(terminal, APIType.ALSI, start=start, end=end)

    def query_lng_lso(self, lso: Union[ALSILSO, str],
                           start: Union[pd.Timestamp, str], end: Union[pd.Timestamp, str]) -> List[Dict]:
        lso = lookup_lso(lso)
        return self._fetch(lso, APIType.ALSI, start=start, end=end)

    def query_lng_country(self, country: Union[ALSICountry, str],
                          start: Union[pd.Timestamp, str], end: Union[pd.Timestamp, str]) -> List[Dict]:
        country = lookup_country_alsi(country)
        return self._fetch(country, APIType.ALSI, start=start, end=end)


class GiePandasClient(GieRawClient):
    def _fix_dataframe(self, data):
        def _fix_values(x):
            x['inventory'] = x['inventory']['lng']
            x['dtmi'] = x['dtmi']['lng']
            return x
        df = pd.DataFrame([_fix_values(x) for x in data])
        for c in ['name', 'code', 'url', 'info']:
            if c in df:
                df = df.drop(columns=c)
        df = df.loc[df['status'] != 'N']
        df['gasDayStart'] = pd.to_datetime(df['gasDayStart'])
        df = df.set_index('gasDayStart')
        # status is only str column, save it for now, convert whole dataframe to float, restore status
        status = df['status'].copy()
        updated_at = pd.to_datetime(df['updatedAt'])
        df = df.drop(columns=['status', 'updatedAt'])
        if 'type' in df:
            df = df.drop(columns=['type'])
        df = df.replace('-', 0).astype(float)
        df['status'] = status
        df['updatedAt'] = updated_at
        return df

    def query_gas_storage(self, storage: Union[AGSIStorage, str],
                          start: Union[pd.Timestamp, str], end: Union[pd.Timestamp, str]) -> pd.DataFrame:
        return self._fix_dataframe(
            super().query_gas_storage(storage=storage, start=start, end=end)
        )

    def query_gas_company(self, company: Union[AGSIStorage, str],
                          start: Union[pd.Timestamp, str], end: Union[pd.Timestamp, str]) -> pd.DataFrame:
        return self._fix_dataframe(
            super().query_gas_company(company=company, start=start, end=end)
        )

    def query_gas_country(self, country: Union[AGSICountry, str],
                      start: Union[pd.Timestamp, str], end: Union[pd.Timestamp, str]) -> pd.DataFrame:
        return self._fix_dataframe(
            super().query_gas_country(country=country, start=start, end=end)
        )

    def query_lng_terminal(self, terminal: Union[ALSITerminal, str],
                           start: Union[pd.Timestamp, str], end: Union[pd.Timestamp, str]) -> pd.DataFrame:
        return self._fix_dataframe(
            super().query_lng_terminal(terminal=terminal, start=start, end=end)
        )

    def query_lng_lso(self, lso: Union[ALSILSO, str],
                           start: Union[pd.Timestamp, str], end: Union[pd.Timestamp, str]) -> pd.DataFrame:
        return self._fix_dataframe(
            super().query_lng_lso(lso=lso, start=start, end=end)
        )

    def query_lng_country(self, country: Union[ALSICountry, str],
                          start: Union[pd.Timestamp, str], end: Union[pd.Timestamp, str]) -> List[Dict]:
        return self._fix_dataframe(
            super().query_lng_country(country=country, start=start, end=end)
        )
