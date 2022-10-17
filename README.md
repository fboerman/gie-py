# gie-py
Python client for the API endpoints of gie.eu. Both ASGI for gas storage and ALSI for LNG terminals and lso's are supported

Using it requires an api key which you can get by registering an account [at the alsi website](https://alsi.gie.eu/#/api).
API keys are valid for both ASGI and ALSI if you set "access to" to "Both ALSI and AGSI+" when registering or later in account settings.

## Installation
`python3 -m pip install gie-py`

## Usage
The package comes with 2 clients:
- [`GieRawClient`](#GieRawClient): Returns data in its raw format direct from api, a list of dictionaries 
- [`GiePandasClient`](#GiePandasClient): Returns data parsed as a Pandas DataFrame

### Supported methods:
The same for both clients. Each method has same setup for arguments, a string to denominate the target 
and a start and end parameter which is either a pandas timestamp or a string
* ```query_gas_storage```
* ```query_gas_company```
* ```query_gas_country```
* ```query_lng_terminal```
* ```query_lng_lso```
* ```query_lng_country```

### Example
```python
from gie import GiePandasClient

client = GiePandasClient(api_key=<YOUR API KEY>)
df_terminal=client.query_lng_terminal('zeebrugge', start='2020-01-01', end='2022-07-10')
df_lso=client.query_lng_lso('fluxys_lng', start='2020-01-01', end='2022-07-10')
```

## meaning of dataframe columns
For the meaning of the columns in the resulting dataframes please consult the official [documentation](https://alsi.gie.eu/GIE_API_documentation_v007.pdf) chapter 2 page 5 and 6