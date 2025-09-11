# oden.ProductAttributesApi

All URIs are relative to *https://api.oden.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_product_attribute_search_post**](ProductAttributesApi.md#v2_product_attribute_search_post) | **POST** /v2/product_attribute/search | 
[**v2_product_attribute_set_post**](ProductAttributesApi.md#v2_product_attribute_set_post) | **POST** /v2/product_attribute/set | 


# **v2_product_attribute_search_post**
> list[ProductAttribute] v2_product_attribute_search_post(product_attribute)



Searches for Product Attributes  Product attributes may be searched by ID, product, or, display_name - in that order.  If an ID is supplied, it will be used to search for a Product Attribute, and display_name, product will be ignored.  If a product is supplied (and no ID), it will be used to search for a Product Attribute, and display_name will be ignored. 

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
    api_instance = oden.ProductAttributesApi(api_client)
    product_attribute = {"product":{"id":"b5da7b1f-3c16-5084-a5da-95b2eba5a4db"}} # ProductAttribute | 

    try:
        api_response = api_instance.v2_product_attribute_search_post(product_attribute)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductAttributesApi->v2_product_attribute_search_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_attribute** | [**ProductAttribute**](ProductAttribute.md)|  | 

### Return type

[**list[ProductAttribute]**](ProductAttribute.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of product attributes - potentially with products and values. |  -  |
**409** | A {match: \&quot;unique\&quot;} was requested, but multiple entities matched the search parameters.  |  -  |
**401** | User has provided either no credentials or invalid credentials |  -  |
**500** | An internal server error has occurred. If reporting the error to Oden, include the ID returned in this response to aid in debugging.  |  -  |
**501** | Endpoint is not yet implemented |  -  |
**400** | An error occurred regarding one of the input parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_product_attribute_set_post**
> list[ProductAttribute] v2_product_attribute_set_post(product_attribute)



Set a Product Attribute for a Product.  If the supplied Product Attribute doesn't exist, it will be created.  If the supplied Product Attribute Value doesn't exist, it will be created.  If the supplied Product Attribute Value is already set for the Product, it will be updated.  If the supplied Product Attribute Value is not set for the Product, it will be added.  Supplied Product must exist already. 

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
    api_instance = oden.ProductAttributesApi(api_client)
    product_attribute = {"product":{"id":"b5da7b1f-3c16-5084-a5da-95b2eba5a4db"},"display_name":"Cable Color","name":"cable_color","value":"Red"} # ProductAttribute | 

    try:
        api_response = api_instance.v2_product_attribute_set_post(product_attribute)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductAttributesApi->v2_product_attribute_set_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_attribute** | [**ProductAttribute**](ProductAttribute.md)|  | 

### Return type

[**list[ProductAttribute]**](ProductAttribute.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of product attributes - potentially with products and values. |  -  |
**409** | A {match: \&quot;unique\&quot;} was requested, but multiple entities matched the search parameters.  |  -  |
**401** | User has provided either no credentials or invalid credentials |  -  |
**500** | An internal server error has occurred. If reporting the error to Oden, include the ID returned in this response to aid in debugging.  |  -  |
**501** | Endpoint is not yet implemented |  -  |
**400** | An error occurred regarding one of the input parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

