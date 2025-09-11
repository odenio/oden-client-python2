# oden.MachineGroupsApi

All URIs are relative to *https://api.oden.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_factory_search_post**](MachineGroupsApi.md#v2_factory_search_post) | **POST** /v2/factory/search | 
[**v2_line_search_post**](MachineGroupsApi.md#v2_line_search_post) | **POST** /v2/line/search | 


# **v2_factory_search_post**
> list[Factory] v2_factory_search_post(factory)



Search for a specific Factory by a unique indentifier: - `name` - `match: unique` or omit  OR  - `id` - `match: unique` or omit  Search for all factories: - `match: all` 

### Example

* Api Key Authentication (APIKeyAuth):
```python
from __future__ import print_function
import time
import oden
from oden.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.oden.app
# See configuration.py for a list of all supported configuration parameters.
configuration = oden.Configuration(
    host = "https://api.oden.app"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyAuth
configuration = oden.Configuration(
    host = "https://api.oden.app",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with oden.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = oden.MachineGroupsApi(api_client)
    factory = {"name":"Factory A"} # Factory | 

    try:
        api_response = api_instance.v2_factory_search_post(factory)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MachineGroupsApi->v2_factory_search_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **factory** | [**Factory**](Factory.md)|  | 

### Return type

[**list[Factory]**](Factory.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of factories. |  -  |
**409** | A {match: \&quot;unique\&quot;} was requested, but multiple entities matched the search parameters.  |  -  |
**401** | User has provided either no credentials or invalid credentials |  -  |
**403** | User has provided valid credentials but is not authorized to access the entity  |  -  |
**500** | An internal server error has occurred. If reporting the error to Oden, include the ID returned in this response to aid in debugging.  |  -  |
**501** | Endpoint is not yet implemented |  -  |
**400** | An error occurred regarding one of the input parameters |  -  |
**404** | Entity not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_line_search_post**
> list[Line] v2_line_search_post(line)



Search for specific Line by any Line identifier. Either: - `id` - `match: unique` or omit  OR - `factory`   - `name` or `id` - line `name` - `match: unique` or omit  Search for all Lines for a given Factory: - `factory`   - `name` or `id` - `match: all` 

### Example

* Api Key Authentication (APIKeyAuth):
```python
from __future__ import print_function
import time
import oden
from oden.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.oden.app
# See configuration.py for a list of all supported configuration parameters.
configuration = oden.Configuration(
    host = "https://api.oden.app"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyAuth
configuration = oden.Configuration(
    host = "https://api.oden.app",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with oden.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = oden.MachineGroupsApi(api_client)
    line = {"match":"all","factory":{"name":"Factory A"}} # Line | 

    try:
        api_response = api_instance.v2_line_search_post(line)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MachineGroupsApi->v2_line_search_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line** | [**Line**](Line.md)|  | 

### Return type

[**list[Line]**](Line.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of lines. |  -  |
**400** | An error occurred regarding one of the input parameters |  -  |
**401** | User has provided either no credentials or invalid credentials |  -  |
**403** | User has provided valid credentials but is not authorized to access the entity  |  -  |
**404** | Entity not found |  -  |
**409** | A {match: \&quot;unique\&quot;} was requested, but multiple entities matched the search parameters.  |  -  |
**500** | An internal server error has occurred. If reporting the error to Oden, include the ID returned in this response to aid in debugging.  |  -  |
**501** | Endpoint is not yet implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

