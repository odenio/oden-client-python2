# oden.StatesApi

All URIs are relative to *https://api.oden.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_state_categories**](StatesApi.md#search_state_categories) | **POST** /v2/state_category/search | Search state categories
[**search_state_reasons**](StatesApi.md#search_state_reasons) | **POST** /v2/state_reason/search | Search state reasons on one or more lines
[**set_state_category**](StatesApi.md#set_state_category) | **POST** /v2/state_category/set | Create or update a state category
[**set_state_reasons**](StatesApi.md#set_state_reasons) | **POST** /v2/state_reason/set | Create a state reason on one or more lines


# **search_state_categories**
> list[StateCategoryDetail] search_state_categories(state_category_search)

Search state categories

Returns the state categories available to your organization, including Oden's built-in ones. Filter by `id` or `name`; omit both to list all. Built-in categories have no `organization` and cannot be modified.  `type` summarises how the platform treats time in the category: - `uptime`: producing good product - `scrapping`: running but not producing good product - `planned_downtime`, `unplanned_downtime`: not running 

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
    api_instance = oden.StatesApi(api_client)
    state_category_search = {} # StateCategorySearch | 

    try:
        # Search state categories
        api_response = api_instance.search_state_categories(state_category_search)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatesApi->search_state_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state_category_search** | [**StateCategorySearch**](StateCategorySearch.md)|  | 

### Return type

[**list[StateCategoryDetail]**](StateCategoryDetail.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The matching state categories. |  -  |
**400** | An error occurred regarding one of the input parameters |  -  |
**401** | User has provided either no credentials or invalid credentials |  -  |
**403** | User has provided valid credentials but is not authorized to access the entity  |  -  |
**500** | An internal server error has occurred. If reporting the error to Oden, include the ID returned in this response to aid in debugging.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_state_reasons**
> list[StateReasonDetail] search_state_reasons(state_reason_search)

Search state reasons on one or more lines

Returns the state reasons defined on every line in `lines` (required; each by `id`, or by `name` plus `factory`), optionally restricted to one `category` (by `id` or `name`). Each result names its line, so one request can audit a whole fleet. Inactive reasons are included, with `active: false`. 

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
    api_instance = oden.StatesApi(api_client)
    state_reason_search = {"lines":[{"id":"2fc8b5e5-fb88-48a7-9c35-4a763206608c"}]} # StateReasonSearch | 

    try:
        # Search state reasons on one or more lines
        api_response = api_instance.search_state_reasons(state_reason_search)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatesApi->search_state_reasons: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state_reason_search** | [**StateReasonSearch**](StateReasonSearch.md)|  | 

### Return type

[**list[StateReasonDetail]**](StateReasonDetail.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The matching state reasons. |  -  |
**400** | An error occurred regarding one of the input parameters |  -  |
**401** | User has provided either no credentials or invalid credentials |  -  |
**403** | User has provided valid credentials but is not authorized to access the entity  |  -  |
**404** | Entity not found |  -  |
**500** | An internal server error has occurred. If reporting the error to Oden, include the ID returned in this response to aid in debugging.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_state_category**
> StateCategoryDetail set_state_category(state_category_set)

Create or update a state category

**Create** (no `id`): `name` and `type` are required. If a category with that `name` already exists for your organization and has the same `type`, it is returned unchanged; a different `type` is a 409.  **Update** (with `id`): fields you omit keep their current value. Built-in categories (no organization) cannot be updated.  Requires an organization admin token. 

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
    api_instance = oden.StatesApi(api_client)
    state_category_set = {"name":"Unplanned Downtime","type":"unplanned_downtime"} # StateCategorySet | 

    try:
        # Create or update a state category
        api_response = api_instance.set_state_category(state_category_set)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatesApi->set_state_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state_category_set** | [**StateCategorySet**](StateCategorySet.md)|  | 

### Return type

[**StateCategoryDetail**](StateCategoryDetail.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The state category after set. |  -  |
**400** | An error occurred regarding one of the input parameters |  -  |
**401** | User has provided either no credentials or invalid credentials |  -  |
**403** | User has provided valid credentials but is not authorized to access the entity  |  -  |
**404** | Entity not found |  -  |
**409** | The entity already exists in a shape that conflicts with the request, or a concurrent request created it and the conflict did not resolve on retry. The message says which.  |  -  |
**500** | An internal server error has occurred. If reporting the error to Oden, include the ID returned in this response to aid in debugging.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_state_reasons**
> list[StateReasonDetail] set_state_reasons(state_reason_set)

Create a state reason on one or more lines

Ensures the reason `name` exists under `category` on every line in `lines`. Lines that already have it are returned as they are; the rest are created in one transaction. The response has one entry per line, in request order, so calling this again is a no-op.  `category` may be given by `id` or `name` and must be one of your organization's own categories; Oden's built-in categories are read-only. `active` defaults to true and also re-activates an existing inactive reason (or deactivates with `false`).  Requires an organization admin token. 

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
    api_instance = oden.StatesApi(api_client)
    state_reason_set = {"lines":[{"id":"2fc8b5e5-fb88-48a7-9c35-4a763206608c"},{"id":"5f1e9c0a-2b7d-4c3e-9a1f-7d2b8e4c6a10"}],"category":{"name":"Unplanned Downtime"},"name":"U108: Equipment - Work Order"} # StateReasonSet | 

    try:
        # Create a state reason on one or more lines
        api_response = api_instance.set_state_reasons(state_reason_set)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatesApi->set_state_reasons: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state_reason_set** | [**StateReasonSet**](StateReasonSet.md)|  | 

### Return type

[**list[StateReasonDetail]**](StateReasonDetail.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The state reason on each requested line. |  -  |
**400** | An error occurred regarding one of the input parameters |  -  |
**401** | User has provided either no credentials or invalid credentials |  -  |
**403** | User has provided valid credentials but is not authorized to access the entity  |  -  |
**404** | Entity not found |  -  |
**409** | The entity already exists in a shape that conflicts with the request, or a concurrent request created it and the conflict did not resolve on retry. The message says which.  |  -  |
**500** | An internal server error has occurred. If reporting the error to Oden, include the ID returned in this response to aid in debugging.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

