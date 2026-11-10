# oden.OQLApi

All URIs are relative to *https://api.oden.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**run_oql_query**](OQLApi.md#run_oql_query) | **POST** /v2/oql/query | Run an OQL query


# **run_oql_query**
> run_oql_query(oql_query, format=format)

Run an OQL query

Run an OQL (Oden Query Language) query.  A 400 means the query itself is wrong: it does not parse, uses an unknown macro or column, has invalid settings, or exceeds the complexity budget. The `error` field says why; fix the query rather than retrying it. A 403 means the caller may not query the lines it touches, and a 412 means the data the query needs is not available yet.  For reference on writing OQL queries, see:  [https://platform.oden.app/knowledge/how-do-i-write-queries-in-oden-query-language-oql](https://platform.oden.app/knowledge/how-do-i-write-queries-in-oden-query-language-oql) 

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
    api_instance = oden.OQLApi(api_client)
    oql_query = oden.OQLQuery() # OQLQuery | 
format = 'json' # str | Format of the response. Can be `json`, `jsonextended` or `csv`. If unspecified, defaults to `jsonextended`.  (optional) (default to 'json')

    try:
        # Run an OQL query
        api_instance.run_oql_query(oql_query, format=format)
    except ApiException as e:
        print("Exception when calling OQLApi->run_oql_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oql_query** | [**OQLQuery**](OQLQuery.md)|  | 
 **format** | **str**| Format of the response. Can be &#x60;json&#x60;, &#x60;jsonextended&#x60; or &#x60;csv&#x60;. If unspecified, defaults to &#x60;jsonextended&#x60;.  | [optional] [default to &#39;json&#39;]

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
**400** | The request is malformed. Either one of the input parameters is invalid (ParameterError body), or this endpoint does not support the combination of inputs supplied (GenericError body, error message prefixed \&quot;Unimplemented:\&quot;).  |  -  |
**401** | User has provided either no credentials or invalid credentials |  -  |
**403** | User has provided valid credentials but is not authorized to access the entity  |  -  |
**404** | Entity not found |  -  |
**409** | A {match: \&quot;unique\&quot;} was requested, but multiple entities matched the search parameters.  |  -  |
**412** | The request is valid, but the data it needs is not available yet.  |  -  |
**429** | Too many requests |  -  |
**500** | An internal server error has occurred. If reporting the error to Oden, include the ID returned in this response to aid in debugging.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

