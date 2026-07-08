# oden.MaintenanceWorkOrdersApi

All URIs are relative to *https://api.oden.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_maintenance_work_order_delete_post**](MaintenanceWorkOrdersApi.md#v2_maintenance_work_order_delete_post) | **POST** /v2/maintenance_work_order/delete | 
[**v2_maintenance_work_order_search_post**](MaintenanceWorkOrdersApi.md#v2_maintenance_work_order_search_post) | **POST** /v2/maintenance_work_order/search | 
[**v2_maintenance_work_order_set_post**](MaintenanceWorkOrdersApi.md#v2_maintenance_work_order_set_post) | **POST** /v2/maintenance_work_order/set | 


# **v2_maintenance_work_order_delete_post**
> list[MaintenanceWorkOrder] v2_maintenance_work_order_delete_post(maintenance_work_order)



Delete a Maintenance Work Order by unique identifier: - `id` OR `external_id` - `match: unique` or omit (only unique is supported) 

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
    api_instance = oden.MaintenanceWorkOrdersApi(api_client)
    maintenance_work_order = {"id":"0012ab4d-1234-123a-8c76-6ea2344be6df"} # MaintenanceWorkOrder | 

    try:
        api_response = api_instance.v2_maintenance_work_order_delete_post(maintenance_work_order)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MaintenanceWorkOrdersApi->v2_maintenance_work_order_delete_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **maintenance_work_order** | [**MaintenanceWorkOrder**](MaintenanceWorkOrder.md)|  | 

### Return type

[**list[MaintenanceWorkOrder]**](MaintenanceWorkOrder.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list containing the deleted maintenance work order. |  -  |
**400** | An error occurred regarding one of the input parameters |  -  |
**401** | User has provided either no credentials or invalid credentials |  -  |
**403** | User has provided valid credentials but is not authorized to access the entity  |  -  |
**404** | Entity not found |  -  |
**409** | A {match: \&quot;unique\&quot;} was requested, but multiple entities matched the search parameters.  |  -  |
**500** | An internal server error has occurred. If reporting the error to Oden, include the ID returned in this response to aid in debugging.  |  -  |
**501** | Endpoint is not yet implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_maintenance_work_order_search_post**
> list[MaintenanceWorkOrder] v2_maintenance_work_order_search_post(inline_object4)



Search for Maintenance Work Orders by: - `id` - `external_id` - `line_id` with required `start_time` and `end_time` filters 

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
    api_instance = oden.MaintenanceWorkOrdersApi(api_client)
    inline_object4 = oden.InlineObject4() # InlineObject4 | 

    try:
        api_response = api_instance.v2_maintenance_work_order_search_post(inline_object4)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MaintenanceWorkOrdersApi->v2_maintenance_work_order_search_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object4** | [**InlineObject4**](InlineObject4.md)|  | 

### Return type

[**list[MaintenanceWorkOrder]**](MaintenanceWorkOrder.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of maintenance work orders. |  -  |
**400** | An error occurred regarding one of the input parameters |  -  |
**401** | User has provided either no credentials or invalid credentials |  -  |
**403** | User has provided valid credentials but is not authorized to access the entity  |  -  |
**404** | Entity not found |  -  |
**409** | A {match: \&quot;unique\&quot;} was requested, but multiple entities matched the search parameters.  |  -  |
**500** | An internal server error has occurred. If reporting the error to Oden, include the ID returned in this response to aid in debugging.  |  -  |
**501** | Endpoint is not yet implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_maintenance_work_order_set_post**
> MaintenanceWorkOrder v2_maintenance_work_order_set_post(maintenance_work_order)



Create or update a Maintenance Work Order.  To **create** a new Maintenance Work Order: - Include `name` and `line`, `external_id`, `started_at` (required) - Omit `id` field - include `completed_at`, `description`, `metadata`  To **update** an existing Maintenance Work Order: - Include the `id` of the existing work order - Include any fields to update  NOTE: Any fields not included in an update request will be left unchanged. 

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
    api_instance = oden.MaintenanceWorkOrdersApi(api_client)
    maintenance_work_order = {"name":"Scheduled Maintenance Q1","line":{"id":"0012ab4d-1234-123a-8c76-6ea2344be6df"},"description":"Quarterly scheduled maintenance","external_id":"MWO-2024-001","started_at":"2024-01-15T08:00:00Z","completed_at":"2024-01-15T17:00:00Z","metadata":"{\"technician\": \"John Doe\", \"priority\": \"high\"}"} # MaintenanceWorkOrder | 

    try:
        api_response = api_instance.v2_maintenance_work_order_set_post(maintenance_work_order)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MaintenanceWorkOrdersApi->v2_maintenance_work_order_set_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **maintenance_work_order** | [**MaintenanceWorkOrder**](MaintenanceWorkOrder.md)|  | 

### Return type

[**MaintenanceWorkOrder**](MaintenanceWorkOrder.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list containing the created or updated maintenance work order. |  -  |
**400** | An error occurred regarding one of the input parameters |  -  |
**401** | User has provided either no credentials or invalid credentials |  -  |
**403** | User has provided valid credentials but is not authorized to access the entity  |  -  |
**404** | Entity not found |  -  |
**409** | A {match: \&quot;unique\&quot;} was requested, but multiple entities matched the search parameters.  |  -  |
**500** | An internal server error has occurred. If reporting the error to Oden, include the ID returned in this response to aid in debugging.  |  -  |
**501** | Endpoint is not yet implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

