[![PyPI version](https://badge.fury.io/py/harmony-connect-client.svg)](https://badge.fury.io/py/harmony-connect-client)
# Factom Harmony Connect - Python Client Library

This is an automatically generated Python client library for [Factom Harmony Connect](https://www.factom.com/products/harmony-connect/).

Connect is the fastest way to add blockchain capabilities to your app without cryptocurrencies, wallets, or network nodes. [Create an account](https://account.factom.com/) to get your free API key for the sandbox environment.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.17
- Package version: 1.0.7
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

For more information, please visit [https://docs.harmony.factom.com](https://docs.harmony.factom.com)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

You can install the Harmony Connect client directly from Github using pip

```sh
pip install git+https://github.com/FactomProject/factom-harmony-connect-python-client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/FactomProject/factom-harmony-connect-python-client.git`)

You can also install the package hosted on PyPi:

```sh
pip install harmony_connect_client
```

Then import the package:
```python
import harmony_connect_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import harmony_connect_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import harmony_connect_client
from harmony_connect_client.rest import ApiException
from pprint import pprint

configuration = harmony_connect_client.Configuration()
# Configure API key authorization: AppId
configuration.api_key['app_id'] = 'YOUR_API_KEY'

configuration = harmony_connect_client.Configuration()
# Configure API key authorization: AppKey
configuration.api_key['app_key'] = 'YOUR_API_KEY'


# create an instance of the API class
api_instance = harmony_connect_client.ChainsApi(harmony_connect_client.ApiClient(configuration))
chain_id = 285904 # str | Chain identifier

try:
    # Get Chain Info
    api_response = api_instance.get_chain_by_id(chain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChainsApi->get_chain_by_id: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://connect-shared-sandbox-2445582615332.production.gw.apicast.io/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ChainsApi* | [**get_chain_by_id**](docs/ChainsApi.md#get_chain_by_id) | **GET** /chains/{chain_id} | Get Chain Info
*ChainsApi* | [**get_chains**](docs/ChainsApi.md#get_chains) | **GET** /chains | Get All Chains
*ChainsApi* | [**post_chain**](docs/ChainsApi.md#post_chain) | **POST** /chains | Create a Chain
*ChainsApi* | [**post_chain_search**](docs/ChainsApi.md#post_chain_search) | **POST** /chains/search | Search Chains
*EntriesApi* | [**get_entries_by_chain_id**](docs/EntriesApi.md#get_entries_by_chain_id) | **GET** /chains/{chain_id}/entries | Get Chain&#39;s Entries
*EntriesApi* | [**get_entry_by_hash**](docs/EntriesApi.md#get_entry_by_hash) | **GET** /chains/{chain_id}/entries/{entry_hash} | Get Entry Info
*EntriesApi* | [**get_first_entry**](docs/EntriesApi.md#get_first_entry) | **GET** /chains/{chain_id}/entries/first | Get Chain&#39;s First Entry
*EntriesApi* | [**get_last_entry**](docs/EntriesApi.md#get_last_entry) | **GET** /chains/{chain_id}/entries/last | Get Chain&#39;s Last Entry
*EntriesApi* | [**post_entries_search**](docs/EntriesApi.md#post_entries_search) | **POST** /chains/{chain_id}/entries/search | Search Chain&#39;s Entries
*EntriesApi* | [**post_entry_to_chain_id**](docs/EntriesApi.md#post_entry_to_chain_id) | **POST** /chains/{chain_id}/entries | Create an Entry
*InfoApi* | [**get_api_info**](docs/InfoApi.md#get_api_info) | **GET** / | API Info


## Documentation For Models

 - [AllInfo](docs/AllInfo.md)
 - [AllInfoLinks](docs/AllInfoLinks.md)
 - [Chain](docs/Chain.md)
 - [ChainCreate](docs/ChainCreate.md)
 - [ChainData](docs/ChainData.md)
 - [ChainDataDblock](docs/ChainDataDblock.md)
 - [ChainDataEblock](docs/ChainDataEblock.md)
 - [ChainDataEntries](docs/ChainDataEntries.md)
 - [ChainLink](docs/ChainLink.md)
 - [ChainList](docs/ChainList.md)
 - [ChainListData](docs/ChainListData.md)
 - [ChainShort](docs/ChainShort.md)
 - [Entry](docs/Entry.md)
 - [EntryCreate](docs/EntryCreate.md)
 - [EntryData](docs/EntryData.md)
 - [EntryDataDblock](docs/EntryDataDblock.md)
 - [EntryDataEblock](docs/EntryDataEblock.md)
 - [EntryList](docs/EntryList.md)
 - [EntryListChain](docs/EntryListChain.md)
 - [EntryListData](docs/EntryListData.md)
 - [EntrySearchResponse](docs/EntrySearchResponse.md)
 - [EntrySearchResponseData](docs/EntrySearchResponseData.md)
 - [EntryShort](docs/EntryShort.md)
 - [SearchBody](docs/SearchBody.md)


## Documentation For Authorization


## AppId

- **Type**: API key
- **API key parameter name**: app_id
- **Location**: HTTP header

## AppKey

- **Type**: API key
- **API key parameter name**: app_key
- **Location**: HTTP header


## Support

For more information, you can view the Connect documentation at [https://docs.harmony.factom.com](https://docs.harmony.factom.com)


For additional support, contact us at harmony-support@factom.com


