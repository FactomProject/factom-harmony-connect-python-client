# harmony_connect_client.ChainsApi

All URIs are relative to *https://connect-shared-sandbox-2445582615332.production.gw.apicast.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_chain_by_id**](ChainsApi.md#get_chain_by_id) | **GET** /chains/{chain_id} | Get Chain Info
[**get_chains**](ChainsApi.md#get_chains) | **GET** /chains | Get All Chains
[**post_chain**](ChainsApi.md#post_chain) | **POST** /chains | Create a Chain
[**post_chain_search**](ChainsApi.md#post_chain_search) | **POST** /chains/search | Search Chains


# **get_chain_by_id**
> Chain get_chain_by_id(chain_id)

Get Chain Info

Get information about a specific chain on Connect

### Example

* Api Key Authentication (AppId): 
```python
from __future__ import print_function
import time
import harmony_connect_client
from harmony_connect_client.rest import ApiException
from pprint import pprint
configuration = harmony_connect_client.Configuration()
# Configure API key authorization: AppId
configuration.api_key['app_id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['app_id'] = 'Bearer'

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


* Api Key Authentication (AppKey): 
```python
from __future__ import print_function
import time
import harmony_connect_client
from harmony_connect_client.rest import ApiException
from pprint import pprint
configuration = harmony_connect_client.Configuration()
# Configure API key authorization: AppKey
configuration.api_key['app_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['app_key'] = 'Bearer'

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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_id** | **str**| Chain identifier | 

### Return type

[**Chain**](Chain.md)

### Authorization

[AppId](../README.md#AppId), [AppKey](../README.md#AppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chains**
> ChainList get_chains(limit=limit, offset=offset, stages=stages)

Get All Chains

Returns all of the chains on factomd.

### Example

* Api Key Authentication (AppId): 
```python
from __future__ import print_function
import time
import harmony_connect_client
from harmony_connect_client.rest import ApiException
from pprint import pprint
configuration = harmony_connect_client.Configuration()
# Configure API key authorization: AppId
configuration.api_key['app_id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['app_id'] = 'Bearer'

# create an instance of the API class
api_instance = harmony_connect_client.ChainsApi(harmony_connect_client.ApiClient(configuration))
limit = 15 # int | The number of items you would like back in each page. (optional)
offset = 2 # int | The offset parameter allows you to select which item you would like to start from when you get back a list from Connect. For example, if you've already seen the first 15 items and you'd like the next set, you would send an offset of 15. `offset=0` starts from the first item of the set and is the default position. (optional)
stages = 'stages_example' # str | The immutability stages you want to restrict results to. You can choose any from `replicated`, `factom`, and `anchored`. If you would like to search among multiple stages, send them in a comma separated string. For example: `'replicated,factom'`. (optional)

try:
    # Get All Chains
    api_response = api_instance.get_chains(limit=limit, offset=offset, stages=stages)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChainsApi->get_chains: %s\n" % e)
```


* Api Key Authentication (AppKey): 
```python
from __future__ import print_function
import time
import harmony_connect_client
from harmony_connect_client.rest import ApiException
from pprint import pprint
configuration = harmony_connect_client.Configuration()
# Configure API key authorization: AppKey
configuration.api_key['app_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['app_key'] = 'Bearer'

# create an instance of the API class
api_instance = harmony_connect_client.ChainsApi(harmony_connect_client.ApiClient(configuration))
limit = 15 # int | The number of items you would like back in each page. (optional)
offset = 2 # int | The offset parameter allows you to select which item you would like to start from when you get back a list from Connect. For example, if you've already seen the first 15 items and you'd like the next set, you would send an offset of 15. `offset=0` starts from the first item of the set and is the default position. (optional)
stages = 'stages_example' # str | The immutability stages you want to restrict results to. You can choose any from `replicated`, `factom`, and `anchored`. If you would like to search among multiple stages, send them in a comma separated string. For example: `'replicated,factom'`. (optional)

try:
    # Get All Chains
    api_response = api_instance.get_chains(limit=limit, offset=offset, stages=stages)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChainsApi->get_chains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The number of items you would like back in each page. | [optional] 
 **offset** | **int**| The offset parameter allows you to select which item you would like to start from when you get back a list from Connect. For example, if you&#39;ve already seen the first 15 items and you&#39;d like the next set, you would send an offset of 15. &#x60;offset&#x3D;0&#x60; starts from the first item of the set and is the default position. | [optional] 
 **stages** | **str**| The immutability stages you want to restrict results to. You can choose any from &#x60;replicated&#x60;, &#x60;factom&#x60;, and &#x60;anchored&#x60;. If you would like to search among multiple stages, send them in a comma separated string. For example: &#x60;&#39;replicated,factom&#39;&#x60;. | [optional] 

### Return type

[**ChainList**](ChainList.md)

### Authorization

[AppId](../README.md#AppId), [AppKey](../README.md#AppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_chain**
> ChainShort post_chain(chain_create)

Create a Chain

Create a new chain. Each chain functions as a mini-blockchain such that all of the entries are linked. Every entry relies on data from previous entries in the chain. Any unauthorized alterations to any of these entries can be detected. Be aware that data entered into the `content` and `external_ids` fields must be in Base64 format. Sending this request will cause Connect to create the first entry of the chain. The data entered into the `content` and `external_id` fields will be applied to this entry.

### Example

* Api Key Authentication (AppId): 
```python
from __future__ import print_function
import time
import harmony_connect_client
from harmony_connect_client.rest import ApiException
from pprint import pprint
configuration = harmony_connect_client.Configuration()
# Configure API key authorization: AppId
configuration.api_key['app_id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['app_id'] = 'Bearer'

# create an instance of the API class
api_instance = harmony_connect_client.ChainsApi(harmony_connect_client.ApiClient(configuration))
chain_create = harmony_connect_client.ChainCreate() # ChainCreate | 

try:
    # Create a Chain
    api_response = api_instance.post_chain(chain_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChainsApi->post_chain: %s\n" % e)
```


* Api Key Authentication (AppKey): 
```python
from __future__ import print_function
import time
import harmony_connect_client
from harmony_connect_client.rest import ApiException
from pprint import pprint
configuration = harmony_connect_client.Configuration()
# Configure API key authorization: AppKey
configuration.api_key['app_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['app_key'] = 'Bearer'

# create an instance of the API class
api_instance = harmony_connect_client.ChainsApi(harmony_connect_client.ApiClient(configuration))
chain_create = harmony_connect_client.ChainCreate() # ChainCreate | 

try:
    # Create a Chain
    api_response = api_instance.post_chain(chain_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChainsApi->post_chain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_create** | [**ChainCreate**](ChainCreate.md)|  | 

### Return type

[**ChainShort**](ChainShort.md)

### Authorization

[AppId](../README.md#AppId), [AppKey](../README.md#AppKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_chain_search**
> ChainList post_chain_search(search_body, limit=limit, offset=offset)

Search Chains

Finds all of the chains with `external_ids` that match what you've entered. External IDs must be sent in Base64 format.

### Example

* Api Key Authentication (AppId): 
```python
from __future__ import print_function
import time
import harmony_connect_client
from harmony_connect_client.rest import ApiException
from pprint import pprint
configuration = harmony_connect_client.Configuration()
# Configure API key authorization: AppId
configuration.api_key['app_id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['app_id'] = 'Bearer'

# create an instance of the API class
api_instance = harmony_connect_client.ChainsApi(harmony_connect_client.ApiClient(configuration))
search_body = harmony_connect_client.SearchBody() # SearchBody | 
limit = 15 # int | The number of items you would like back in each page. (optional)
offset = 2 # int | The offset parameter allows you to select which item you would like to start from when you get back a list from Connect. For example, if you've already seen the first 15 items and you'd like the next set, you would send an offset of 15. `offset=0` starts from the first item of the set and is the default position. (optional)

try:
    # Search Chains
    api_response = api_instance.post_chain_search(search_body, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChainsApi->post_chain_search: %s\n" % e)
```


* Api Key Authentication (AppKey): 
```python
from __future__ import print_function
import time
import harmony_connect_client
from harmony_connect_client.rest import ApiException
from pprint import pprint
configuration = harmony_connect_client.Configuration()
# Configure API key authorization: AppKey
configuration.api_key['app_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['app_key'] = 'Bearer'

# create an instance of the API class
api_instance = harmony_connect_client.ChainsApi(harmony_connect_client.ApiClient(configuration))
search_body = harmony_connect_client.SearchBody() # SearchBody | 
limit = 15 # int | The number of items you would like back in each page. (optional)
offset = 2 # int | The offset parameter allows you to select which item you would like to start from when you get back a list from Connect. For example, if you've already seen the first 15 items and you'd like the next set, you would send an offset of 15. `offset=0` starts from the first item of the set and is the default position. (optional)

try:
    # Search Chains
    api_response = api_instance.post_chain_search(search_body, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChainsApi->post_chain_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_body** | [**SearchBody**](SearchBody.md)|  | 
 **limit** | **int**| The number of items you would like back in each page. | [optional] 
 **offset** | **int**| The offset parameter allows you to select which item you would like to start from when you get back a list from Connect. For example, if you&#39;ve already seen the first 15 items and you&#39;d like the next set, you would send an offset of 15. &#x60;offset&#x3D;0&#x60; starts from the first item of the set and is the default position. | [optional] 

### Return type

[**ChainList**](ChainList.md)

### Authorization

[AppId](../README.md#AppId), [AppKey](../README.md#AppKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

