# oden.DashboardsApi

All URIs are relative to *https://api.oden.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute_dashboard**](DashboardsApi.md#execute_dashboard) | **POST** /v2/dashboard/execute | Execute a dashboard


# **execute_dashboard**
> list[DashboardExecuteResult] execute_dashboard(dashboard_execute_request)

Execute a dashboard

Execute every module in a dashboard with shared time-range and filter overrides, returning the columns and rows produced by each module.  Modules execute in parallel and are reported in the dashboard's stored module order. Per-module failures (parse, dispatch) land in the `error` field of that module's result; siblings continue to run.  Known v1 limitations: - Template variables (`{var_name}` in stored OQL) are not substituted   server-side. Modules containing unsubstituted placeholders will   fail at parse time. 

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
    api_instance = oden.DashboardsApi(api_client)
    dashboard_execute_request = oden.DashboardExecuteRequest() # DashboardExecuteRequest | 

    try:
        # Execute a dashboard
        api_response = api_instance.execute_dashboard(dashboard_execute_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardsApi->execute_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_execute_request** | [**DashboardExecuteRequest**](DashboardExecuteRequest.md)|  | 

### Return type

[**list[DashboardExecuteResult]**](DashboardExecuteResult.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dashboard loaded and each module executed. Individual modules may still report &#x60;error&#x60; in their result; this is not a 200/non-200 distinction.  |  -  |
**400** | An error occurred regarding one of the input parameters |  -  |
**401** | User has provided either no credentials or invalid credentials |  -  |
**403** | User has provided valid credentials but is not authorized to access the entity  |  -  |
**404** | Entity not found |  -  |
**429** | Too many requests |  -  |
**500** | An internal server error has occurred. If reporting the error to Oden, include the ID returned in this response to aid in debugging.  |  -  |
**501** | Endpoint is not yet implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

