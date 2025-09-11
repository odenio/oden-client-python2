# oden.QualityTestApi

All URIs are relative to *https://api.oden.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_quality_schema_search_post**](QualityTestApi.md#v2_quality_schema_search_post) | **POST** /v2/quality_schema/search | 
[**v2_quality_test_delete_post**](QualityTestApi.md#v2_quality_test_delete_post) | **POST** /v2/quality_test/delete | 
[**v2_quality_test_search_post**](QualityTestApi.md#v2_quality_test_search_post) | **POST** /v2/quality_test/search | 
[**v2_quality_test_set_post**](QualityTestApi.md#v2_quality_test_set_post) | **POST** /v2/quality_test/set | 
[**v2_quality_tests_delete_post**](QualityTestApi.md#v2_quality_tests_delete_post) | **POST** /v2/quality_tests/delete | 


# **v2_quality_schema_search_post**
> v2_quality_schema_search_post(quality_schema)



Searches for Quality Schema[s] by:  - `factory` 

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
    api_instance = oden.QualityTestApi(api_client)
    quality_schema = {"factory":{"name":"Factory A"}} # QualitySchema | 

    try:
        api_instance.v2_quality_schema_search_post(quality_schema)
    except ApiException as e:
        print("Exception when calling QualityTestApi->v2_quality_schema_search_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quality_schema** | [**QualitySchema**](QualitySchema.md)|  | 

### Return type

void (empty response body)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**409** | A {match: \&quot;unique\&quot;} was requested, but multiple entities matched the search parameters.  |  -  |
**401** | User has provided either no credentials or invalid credentials |  -  |
**403** | User has provided valid credentials but is not authorized to access the entity  |  -  |
**500** | An internal server error has occurred. If reporting the error to Oden, include the ID returned in this response to aid in debugging.  |  -  |
**501** | Endpoint is not yet implemented |  -  |
**400** | An error occurred regarding one of the input parameters |  -  |
**404** | Entity not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_quality_test_delete_post**
> v2_quality_test_delete_post(quality_test)



Searches for uniqueQuality Test by:  - `id`  OR  - `interval` (of type `RUN` or `BATCH`)*  *This only work if there is a single quality test record for the interval. 

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
    api_instance = oden.QualityTestApi(api_client)
    quality_test = {"id":"16a8fa1f-ba0a-4040-81c9-ac4dd054bdbb","match":"unique"} # QualityTest | 

    try:
        api_instance.v2_quality_test_delete_post(quality_test)
    except ApiException as e:
        print("Exception when calling QualityTestApi->v2_quality_test_delete_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quality_test** | [**QualityTest**](QualityTest.md)|  | 

### Return type

void (empty response body)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**409** | A {match: \&quot;unique\&quot;} was requested, but multiple entities matched the search parameters.  |  -  |
**401** | User has provided either no credentials or invalid credentials |  -  |
**403** | User has provided valid credentials but is not authorized to access the entity  |  -  |
**500** | An internal server error has occurred. If reporting the error to Oden, include the ID returned in this response to aid in debugging.  |  -  |
**501** | Endpoint is not yet implemented |  -  |
**400** | An error occurred regarding one of the input parameters |  -  |
**404** | Entity not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_quality_test_search_post**
> v2_quality_test_search_post(quality_test)



Searches for Quality Test[s] by:  - `id`  OR  - `interval` (of type `RUN` or `BATCH`) 

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
    api_instance = oden.QualityTestApi(api_client)
    quality_test = {"id":"16a8fa1f-ba0a-4040-81c9-ac4dd054bdbb","match":"unique"} # QualityTest | 

    try:
        api_instance.v2_quality_test_search_post(quality_test)
    except ApiException as e:
        print("Exception when calling QualityTestApi->v2_quality_test_search_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quality_test** | [**QualityTest**](QualityTest.md)|  | 

### Return type

void (empty response body)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**409** | A {match: \&quot;unique\&quot;} was requested, but multiple entities matched the search parameters.  |  -  |
**401** | User has provided either no credentials or invalid credentials |  -  |
**403** | User has provided valid credentials but is not authorized to access the entity  |  -  |
**500** | An internal server error has occurred. If reporting the error to Oden, include the ID returned in this response to aid in debugging.  |  -  |
**501** | Endpoint is not yet implemented |  -  |
**400** | An error occurred regarding one of the input parameters |  -  |
**404** | Entity not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_quality_test_set_post**
> v2_quality_test_set_post(quality_test)



Create or update a Quality Test record: - To update `id` must be supplied. Only the supplied fields will be updated, the rest will remain unchanged. - If `id` is not supplied, a new `quality_test_record` will be created. 

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
    api_instance = oden.QualityTestApi(api_client)
    quality_test = {"interval":{"id":"178a61c0f00","line":{"factory":{"id":"e32d004e-ce8b-40bf-bbc1-14fd907d2f47"},"name":"Line 01"},"type":{"id":"e07da9a8-f2fd-480c-a315-d4c84fcac08c","name":"BATCH"}},"quality_schema":{"id":"66"},"raw_data":{"fdr":"test string 3","impedance":6.789,"test_length":10,"test_rl":"test string"},"timestamp":"2022-02-18T16:28:04Z"} # QualityTest | 

    try:
        api_instance.v2_quality_test_set_post(quality_test)
    except ApiException as e:
        print("Exception when calling QualityTestApi->v2_quality_test_set_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quality_test** | [**QualityTest**](QualityTest.md)|  | 

### Return type

void (empty response body)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**409** | A {match: \&quot;unique\&quot;} was requested, but multiple entities matched the search parameters.  |  -  |
**401** | User has provided either no credentials or invalid credentials |  -  |
**403** | User has provided valid credentials but is not authorized to access the entity  |  -  |
**500** | An internal server error has occurred. If reporting the error to Oden, include the ID returned in this response to aid in debugging.  |  -  |
**501** | Endpoint is not yet implemented |  -  |
**400** | An error occurred regarding one of the input parameters |  -  |
**404** | Entity not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_quality_tests_delete_post**
> v2_quality_tests_delete_post(inline_object3)



Bulk deletes quality tests, either: - All quality tests on a given `line` whose `timsetamp` is between `start_time` and `end_time` OR - All quality tests whose `id` is supplied  It will do one or the other, with a bias for `id`'s if both are supplied. 

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
    api_instance = oden.QualityTestApi(api_client)
    inline_object3 = oden.InlineObject3() # InlineObject3 | 

    try:
        api_instance.v2_quality_tests_delete_post(inline_object3)
    except ApiException as e:
        print("Exception when calling QualityTestApi->v2_quality_tests_delete_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object3** | [**InlineObject3**](InlineObject3.md)|  | 

### Return type

void (empty response body)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**409** | A {match: \&quot;unique\&quot;} was requested, but multiple entities matched the search parameters.  |  -  |
**401** | User has provided either no credentials or invalid credentials |  -  |
**403** | User has provided valid credentials but is not authorized to access the entity  |  -  |
**500** | An internal server error has occurred. If reporting the error to Oden, include the ID returned in this response to aid in debugging.  |  -  |
**501** | Endpoint is not yet implemented |  -  |
**400** | An error occurred regarding one of the input parameters |  -  |
**404** | Entity not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

