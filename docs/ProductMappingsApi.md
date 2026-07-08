# oden.ProductMappingsApi

All URIs are relative to *https://api.oden.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_product_mapping_search_post**](ProductMappingsApi.md#v2_product_mapping_search_post) | **POST** /v2/product_mapping/search | 
[**v2_product_mapping_set_post**](ProductMappingsApi.md#v2_product_mapping_set_post) | **POST** /v2/product_mapping/set | 


# **v2_product_mapping_search_post**
> list[ProductMapping] v2_product_mapping_search_post(product_mapping)



Searches for Product Mappings.  May be used to confirm a Product Mapping exists.  Much like `product/search`, may be used to get `name`s of line or product from `id`s, or `id`s from `name`s. 

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
    api_instance = oden.ProductMappingsApi(api_client)
    product_mapping = {"line":{"id":"2fc8b5e5-fb88-48a7-9c35-4a763206608c"},"product":{"id":"b5da7b1f-3c16-5084-a5da-95b2eba5a4db"}} # ProductMapping | 

    try:
        api_response = api_instance.v2_product_mapping_search_post(product_mapping)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductMappingsApi->v2_product_mapping_search_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_mapping** | [**ProductMapping**](ProductMapping.md)|  | 

### Return type

[**list[ProductMapping]**](ProductMapping.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of product mappings. |  -  |
**409** | A {match: \&quot;unique\&quot;} was requested, but multiple entities matched the search parameters.  |  -  |
**401** | User has provided either no credentials or invalid credentials |  -  |
**500** | An internal server error has occurred. If reporting the error to Oden, include the ID returned in this response to aid in debugging.  |  -  |
**501** | Endpoint is not yet implemented |  -  |
**400** | An error occurred regarding one of the input parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_product_mapping_set_post**
> v2_product_mapping_set_post(product_mapping)



Map a Product to a Line - implying this Line can produce, or is producing this Product.  If the supplied Product doesn't exist, it will be created. 

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
    api_instance = oden.ProductMappingsApi(api_client)
    product_mapping = {"line":{"id":"2fc8b5e5-fb88-48a7-9c35-4a763206608c"},"product":{"id":"b5da7b1f-3c16-5084-a5da-95b2eba5a4db"}} # ProductMapping | 

    try:
        api_instance.v2_product_mapping_set_post(product_mapping)
    except ApiException as e:
        print("Exception when calling ProductMappingsApi->v2_product_mapping_set_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_mapping** | [**ProductMapping**](ProductMapping.md)|  | 

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
**500** | An internal server error has occurred. If reporting the error to Oden, include the ID returned in this response to aid in debugging.  |  -  |
**501** | Endpoint is not yet implemented |  -  |
**400** | An error occurred regarding one of the input parameters |  -  |
**404** | Entity not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

