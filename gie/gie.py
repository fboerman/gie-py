import requests
import pandas as pd
from typing import List, Dict, Union
from .mappings import ASGICompany, ASGIStorage, lookup_company, lookup_storage
from enum import Enum

__title__ = "gie-py"
__version__ = "0.1.0"
__author__ = "Frank Boerman"
__license__ = "MIT"


class APIType(str, Enum):
    ASGI = "https://agsi.gie.eu/api/data/"
    ALSGI = "https://alsi.gie.eu/api/data/"


class GieRawClient:
    def __init__(self, api_key):
        self.s = requests.Session()
        self.s.headers.update({
            'user-agent': 'gie-py (github.com/fboerman/gie-py)',
            'x-key': api_key
        })

    def _fetch(self, url: str, t: APIType,
               start: Union[pd.Timestamp, str], end: Union[pd.Timestamp, str]):
        if type(start) != pd.Timestamp:
            start = pd.Timestamp(start)
        if type(end) != pd.Timestamp:
            end = pd.Timestamp(end)

        r = self.s.get(t.value + url, params={
            'from': start.strftime('%Y-%m-%d'),
            'till': end.strftime('%Y-%m-%d')
        })
        r.raise_for_status()

        if t == APIType.ASGI:
            return r.json()['data']
        else:
            return r.json()

    def query_gas_storage(self, storage: Union[ASGIStorage, str],
                          start: Union[pd.Timestamp, str], end: Union[pd.Timestamp, str]) -> List[Dict]:
        storage = lookup_storage(storage)
        return self._fetch(storage.get_url(), APIType.ASGI, start=start, end=end)

    def query_gas_company(self, company: Union[ASGICompany, str],
                          start: Union[pd.Timestamp, str], end: Union[pd.Timestamp, str]) -> List[Dict]:
        company = lookup_company(company)
        return self._fetch(company.get_url(), APIType.ASGI, start=start, end=end)


class GiePandasClient(GieRawClient):
    def _fix_asgi_dataframe(self, data):
        df = pd.DataFrame(data).drop(columns=['name', 'code', 'url', 'info'])
        df['gasDayStart'] = pd.to_datetime(df['gasDayStart'])
        df = df.set_index('gasDayStart')
        # status is only str column, save it for now, convert whole dataframe to float, restore status
        status = df['status'].copy()
        df = df.drop(columns=['status']).astype(float)
        df['status'] = status

        return df

    def query_gas_storage(self, storage: Union[ASGIStorage, str],
                          start: Union[pd.Timestamp, str], end: Union[pd.Timestamp, str]) -> pd.DataFrame:
        return self._fix_asgi_dataframe(
            super().query_gas_storage(storage=storage, start=start, end=end)
        )

    def query_gas_company(self, company: Union[ASGIStorage, str],
                          start: Union[pd.Timestamp, str], end: Union[pd.Timestamp, str]) -> pd.DataFrame:
        return self._fix_asgi_dataframe(
            super().query_gas_company(company=company, start=start, end=end)
        )
