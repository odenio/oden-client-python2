# oden
The Oden Private Partner API exposes RESTful API endpoints for clients to get, create and update data on the Oden Platform.

The API is based on the OpenAPI 3.0 specification.
### Current Version
The URL, and host, for the current version is [https://api.oden.app/v2](https://api.oden.app/v2).

### Oden's Data Model
- **Organization**: This represents the Organization registered as an Oden customer. An organization has an associated collection of users, factories, lines, etc. This is the entity a specific authentication token is associated with.
- **Asset** or **Machinegroup**: Assets, or machinegroups, are collections of machines, which may either be a **Factory** or a **Line**:
  - **Factory**: Factories are collections of lines, representing a particular manufacturing location.
    - **Line**: Lines are collections of machines, often representing a particular production line. Lines may also have **Products** mapped to them, indicating what is currently being manufactured by the specific line.
      - **Machine**: Machines are the physical machines that make up a line
- **Product**: Products capture what entities a manufacturer produces
- **Interval**: An interval is a period of time that takes place on a manufacturing line and expresses some business concern. It's Oden's way of making metrics aggregatable, traceable, and relatable to a manufacturer.
  - **Run**: A run is a production interval that labels a period of production as being work on some single product
  - **Batch**: A batch is a production interval that represents a portion of a particular run
  - **State**: A state is an interval that tracks the availability or utilization of a line
    - **State Category**: A state category describes what state a line is in - such as ex. uptime, downtime, scrapping, etc.
    - **State Reason**: A state reason describes why a line is in a particular state - such as \"maintenance\" being a reason for the category \"downtime\".
  - **Custom**: A custom interval can track any other type of interval-based data a manufacturer might want to analyze. These are created on a per-factory basis.
- **Target**: Targets specify values and upper/lower thresholds for metrics when specific products are running on specific lines
- **Scrap/Yield**: Scrap/yield output specifies amount of produced product on a line during either a run or batch interval. Oden will categorize all output as either scrap or yield - as specified by the Scrap Yield Schema for a given factory. If you have other categories, like rework/blocked/off-grade, you must choose between categorizing those amounts as either good or bad production by specifying as scrap or yield. Clients may also add scrap codes (i.e., reasons) to a given Scrap Yield Data entry.
  - **Scrap Code**: A scrap code is a code that explains the reason for a scrap/yield raw data input - such as \"Rework\"
- **Quality Test**: Quality Tests are results of quality assurance tests done on site, and uploaded to Oden. They may be attached to a single Batch or Run.
- **Metric**: Known in factories as \"tags\", metrics are the raw data that is collected by Oden from the machines and devices on the factory floor.
- **Metric Group**: Metric groups are metrics that represent the same thing across different lines. They provide common display names for tags and allow labeling groups of tags as measuring key types of data like performance or production.

### Best Practices
Under the current implementation, the Oden API does not rate limit requests from clients.

However, rate limiting will be introduced in the near future and it is recommended that users design their API
clients to not exceed a request rate of **one per second**.

### Schema
All v2 API access is over HTTPS and accessed from https://api.oden.app/v2
All data is sent and received as JSON.

API requests with duplicate keys will process only the data for the first key detected and ignore the rest, so it's not recommended. Batching multiple messages in this way is currently not possible.
  - Example of duplicate key in JSON: {\"raw_data\":{\"scrap\":\"10\",\"scrap\":\"100\"}}

All timestamps are returned in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#Times) format:

  `YYYY-MM-DDTHH:MM:SSZ`

All durations are returned in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#Times) format with the largest unit of time being the hour:

   `PT[n]H[n]M[n]S`

All timestamps sent to the API in POST requests should be in ISO 8601 format.
### HTTP Verbs
The ONLY HTTP call type (sometimes called *verb* or *method*) used within Oden's API is **POST**.
There are three actions supported via a **POST**; call, search, set, and delete, together supporting CRUD operations;
  - **search** requests are used to search for and *read* objects in the Oden Platform
      - All Oden Objects may be uniquely identified by some combination of, or a single, parameter.
        - Ex a `line` my be identified by either:
          - `id`
          - `name` AND `factory`
  - **set** requests are used to *create* or *update* objects
  - **delete** requests are used to *delete* objects. If a delete endpoint is not yet implemented for a given object, users may choose to update the values of a specific entity to null or 0 values.

### URI Components
All endpoints may be accessed with the URI pattern:
`https://api.oden.app/v2/{object}/{action}`

Where:
  - `object` is the name of the object being requested:
       - `factory`, `quality_test`, `interval`, `line`, etc...
  - `action` is the name of the action being requested
    - `search` , `set` , `delete`

e.g. `https://api.oden.app/v2/factory/search`

# Authentication
Clients can authenticate through the v2 API using a Token provided by Oden. Tokens are opaque strings similar to
[Bearer](https://swagger.io/docs/specification/authentication/bearer-authentication/) tokens that the client must
pass in the [HTTP Authorization request header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization) in every request.
The syntax is as follows:

`Authorization: <type> <credentials>`

Where \\<type\\> is \"Token\" and \\<credentials\\> is the Token string. For example:

`Authorization: Token tokenStringProvidedByOden`

Authenticating with an invalid Token will return `401 Unauthorized Error`.

Authenticating with a Token that is not authorized to read requested data will return `403 Forbidden Error`.

Some endpoints may require requests to be broken out by machinegroup (i.e., line or factory) and the number of
requests would scale accordingly. This multiplicity should be taken into consideration when deciding on the
frequency the API client makes requests to the Oden endpoints.

To authenticate in this [UI](https://api.oden.app/v2/ui/), click the Lock icon, and copy/paste the token into the Authorize box.


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://oden.io/contact/](https://oden.io/contact/)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/odenio/oden-client-python2.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/odenio/oden-client-python2.git`)

Then import the package:
```python
import oden
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import oden
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
    api_instance = oden.IntervalsApi(api_client)
    interval = {"id":"<REPLACE_WITH_ACTUAL_RUN_UUID>","line":{"id":"2fc8b5e5-fb88-48a7-9c35-4a763206608c"},"type":{"name":"RUN"}} # Interval | 

    try:
        api_response = api_instance.v2_interval_delete_post(interval)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IntervalsApi->v2_interval_delete_post: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *https://api.oden.app*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*IntervalsApi* | [**v2_interval_delete_post**](docs/IntervalsApi.md#v2_interval_delete_post) | **POST** /v2/interval/delete | 
*IntervalsApi* | [**v2_interval_search_post**](docs/IntervalsApi.md#v2_interval_search_post) | **POST** /v2/interval/search | 
*IntervalsApi* | [**v2_interval_set_post**](docs/IntervalsApi.md#v2_interval_set_post) | **POST** /v2/interval/set | 
*IntervalsApi* | [**v2_interval_type_search_post**](docs/IntervalsApi.md#v2_interval_type_search_post) | **POST** /v2/interval_type/search | 
*IntervalsApi* | [**v2_intervals_delete_post**](docs/IntervalsApi.md#v2_intervals_delete_post) | **POST** /v2/intervals/delete | 
*IntervalsApi* | [**v2_intervals_set_post**](docs/IntervalsApi.md#v2_intervals_set_post) | **POST** /v2/intervals/set | 
*MachineGroupsApi* | [**v2_factory_search_post**](docs/MachineGroupsApi.md#v2_factory_search_post) | **POST** /v2/factory/search | 
*MachineGroupsApi* | [**v2_line_search_post**](docs/MachineGroupsApi.md#v2_line_search_post) | **POST** /v2/line/search | 
*MetricGroupsApi* | [**v2_metric_group_search_post**](docs/MetricGroupsApi.md#v2_metric_group_search_post) | **POST** /v2/metric_group/search | 
*OQLApi* | [**v2_oql_query_post**](docs/OQLApi.md#v2_oql_query_post) | **POST** /v2/oql/query | 
*ProductAttributesApi* | [**v2_product_attribute_search_post**](docs/ProductAttributesApi.md#v2_product_attribute_search_post) | **POST** /v2/product_attribute/search | 
*ProductAttributesApi* | [**v2_product_attribute_set_post**](docs/ProductAttributesApi.md#v2_product_attribute_set_post) | **POST** /v2/product_attribute/set | 
*ProductMappingsApi* | [**v2_product_mapping_search_post**](docs/ProductMappingsApi.md#v2_product_mapping_search_post) | **POST** /v2/product_mapping/search | 
*ProductMappingsApi* | [**v2_product_mapping_set_post**](docs/ProductMappingsApi.md#v2_product_mapping_set_post) | **POST** /v2/product_mapping/set | 
*ProductsApi* | [**v2_product_delete_post**](docs/ProductsApi.md#v2_product_delete_post) | **POST** /v2/product/delete | 
*ProductsApi* | [**v2_product_search_post**](docs/ProductsApi.md#v2_product_search_post) | **POST** /v2/product/search | 
*ProductsApi* | [**v2_product_set_post**](docs/ProductsApi.md#v2_product_set_post) | **POST** /v2/product/set | 
*QualityTestApi* | [**v2_quality_schema_search_post**](docs/QualityTestApi.md#v2_quality_schema_search_post) | **POST** /v2/quality_schema/search | 
*QualityTestApi* | [**v2_quality_test_delete_post**](docs/QualityTestApi.md#v2_quality_test_delete_post) | **POST** /v2/quality_test/delete | 
*QualityTestApi* | [**v2_quality_test_search_post**](docs/QualityTestApi.md#v2_quality_test_search_post) | **POST** /v2/quality_test/search | 
*QualityTestApi* | [**v2_quality_test_set_post**](docs/QualityTestApi.md#v2_quality_test_set_post) | **POST** /v2/quality_test/set | 
*QualityTestApi* | [**v2_quality_tests_delete_post**](docs/QualityTestApi.md#v2_quality_tests_delete_post) | **POST** /v2/quality_tests/delete | 
*ScrapYieldDataApi* | [**v2_scrap_yield_delete_post**](docs/ScrapYieldDataApi.md#v2_scrap_yield_delete_post) | **POST** /v2/scrap_yield/delete | 
*ScrapYieldDataApi* | [**v2_scrap_yield_search_post**](docs/ScrapYieldDataApi.md#v2_scrap_yield_search_post) | **POST** /v2/scrap_yield/search | 
*ScrapYieldDataApi* | [**v2_scrap_yield_set_post**](docs/ScrapYieldDataApi.md#v2_scrap_yield_set_post) | **POST** /v2/scrap_yield/set | 
*TargetsApi* | [**v2_target_search_post**](docs/TargetsApi.md#v2_target_search_post) | **POST** /v2/target/search | 
*TargetsApi* | [**v2_target_set_post**](docs/TargetsApi.md#v2_target_set_post) | **POST** /v2/target/set | 


## Documentation For Models

 - [BatchMetadata](docs/BatchMetadata.md)
 - [Factory](docs/Factory.md)
 - [GenericError](docs/GenericError.md)
 - [InlineObject](docs/InlineObject.md)
 - [InlineObject1](docs/InlineObject1.md)
 - [InlineObject2](docs/InlineObject2.md)
 - [InlineObject3](docs/InlineObject3.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse400](docs/InlineResponse400.md)
 - [InlineResponse409](docs/InlineResponse409.md)
 - [InlineResponse500](docs/InlineResponse500.md)
 - [Interval](docs/Interval.md)
 - [IntervalBulkCreate](docs/IntervalBulkCreate.md)
 - [IntervalBulkDelete](docs/IntervalBulkDelete.md)
 - [IntervalType](docs/IntervalType.md)
 - [Line](docs/Line.md)
 - [Match](docs/Match.md)
 - [MetricGroup](docs/MetricGroup.md)
 - [OQLQuery](docs/OQLQuery.md)
 - [Product](docs/Product.md)
 - [ProductAttribute](docs/ProductAttribute.md)
 - [ProductMapping](docs/ProductMapping.md)
 - [QualitySchema](docs/QualitySchema.md)
 - [QualityTest](docs/QualityTest.md)
 - [RunMetadata](docs/RunMetadata.md)
 - [ScrapYieldData](docs/ScrapYieldData.md)
 - [ScrapYieldSchema](docs/ScrapYieldSchema.md)
 - [StateCategory](docs/StateCategory.md)
 - [StateMetadata](docs/StateMetadata.md)
 - [StateReason](docs/StateReason.md)
 - [Target](docs/Target.md)
 - [Unit](docs/Unit.md)


## Documentation For Authorization


## APIKeyAuth

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

support@oden.io


