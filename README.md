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
- **Maintenance Work Order**: A maintenance work order can be used to track work orders maintained in MaintainX and associate them with an Oden line. 

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
    api_instance = oden.DashboardsApi(api_client)
    dashboard_execute_request = oden.DashboardExecuteRequest() # DashboardExecuteRequest | 

    try:
        # Execute a dashboard
        api_response = api_instance.execute_dashboard(dashboard_execute_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardsApi->execute_dashboard: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *https://api.oden.app*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DashboardsApi* | [**execute_dashboard**](docs/DashboardsApi.md#execute_dashboard) | **POST** /v2/dashboard/execute | Execute a dashboard
*IntervalsApi* | [**bulk_delete_intervals**](docs/IntervalsApi.md#bulk_delete_intervals) | **POST** /v2/intervals/delete | Delete intervals in a time range
*IntervalsApi* | [**bulk_set_intervals**](docs/IntervalsApi.md#bulk_set_intervals) | **POST** /v2/intervals/set | Create a set of intervals
*IntervalsApi* | [**bulk_update_intervals**](docs/IntervalsApi.md#bulk_update_intervals) | **POST** /v2/intervals/update | Update a set of intervals
*IntervalsApi* | [**delete_interval**](docs/IntervalsApi.md#delete_interval) | **POST** /v2/interval/delete | Delete an interval
*IntervalsApi* | [**delete_interval_type**](docs/IntervalsApi.md#delete_interval_type) | **POST** /v2/interval_type/delete | Delete a custom interval type
*IntervalsApi* | [**search_interval_types**](docs/IntervalsApi.md#search_interval_types) | **POST** /v2/interval_type/search | Search interval types
*IntervalsApi* | [**search_intervals**](docs/IntervalsApi.md#search_intervals) | **POST** /v2/interval/search | Search intervals on a line
*IntervalsApi* | [**set_interval**](docs/IntervalsApi.md#set_interval) | **POST** /v2/interval/set | Create or update an interval
*IntervalsApi* | [**set_interval_type**](docs/IntervalsApi.md#set_interval_type) | **POST** /v2/interval_type/set | Create or update a custom interval type
*IntervalsApi* | [**update_interval**](docs/IntervalsApi.md#update_interval) | **POST** /v2/interval/update | Update an interval
*MachineGroupsApi* | [**search_factories**](docs/MachineGroupsApi.md#search_factories) | **POST** /v2/factory/search | Search factories
*MachineGroupsApi* | [**search_lines**](docs/MachineGroupsApi.md#search_lines) | **POST** /v2/line/search | Search production lines
*MaintenanceWorkOrdersApi* | [**delete_maintenance_work_order**](docs/MaintenanceWorkOrdersApi.md#delete_maintenance_work_order) | **POST** /v2/maintenance_work_order/delete | Delete a maintenance work order
*MaintenanceWorkOrdersApi* | [**search_maintenance_work_orders**](docs/MaintenanceWorkOrdersApi.md#search_maintenance_work_orders) | **POST** /v2/maintenance_work_order/search | Search maintenance work orders
*MaintenanceWorkOrdersApi* | [**set_maintenance_work_order**](docs/MaintenanceWorkOrdersApi.md#set_maintenance_work_order) | **POST** /v2/maintenance_work_order/set | Create or update a maintenance work order
*MetricGroupsApi* | [**search_metric_groups**](docs/MetricGroupsApi.md#search_metric_groups) | **POST** /v2/metric_group/search | Search metric groups
*OQLApi* | [**run_oql_query**](docs/OQLApi.md#run_oql_query) | **POST** /v2/oql/query | Run an OQL query
*ProductAttributesApi* | [**search_product_attributes**](docs/ProductAttributesApi.md#search_product_attributes) | **POST** /v2/product_attribute/search | Search product attributes
*ProductAttributesApi* | [**set_product_attribute**](docs/ProductAttributesApi.md#set_product_attribute) | **POST** /v2/product_attribute/set | Create or update a product attribute
*ProductMappingsApi* | [**search_product_mappings**](docs/ProductMappingsApi.md#search_product_mappings) | **POST** /v2/product_mapping/search | Search product-to-line mappings
*ProductMappingsApi* | [**set_product_mapping**](docs/ProductMappingsApi.md#set_product_mapping) | **POST** /v2/product_mapping/set | Map a product to a line
*ProductsApi* | [**delete_product**](docs/ProductsApi.md#delete_product) | **POST** /v2/product/delete | Delete a product
*ProductsApi* | [**search_products**](docs/ProductsApi.md#search_products) | **POST** /v2/product/search | Search products
*ProductsApi* | [**set_product**](docs/ProductsApi.md#set_product) | **POST** /v2/product/set | Create or update a product
*QualityTestApi* | [**bulk_delete_quality_tests**](docs/QualityTestApi.md#bulk_delete_quality_tests) | **POST** /v2/quality_tests/delete | Delete multiple quality tests
*QualityTestApi* | [**delete_quality_test**](docs/QualityTestApi.md#delete_quality_test) | **POST** /v2/quality_test/delete | Delete a quality test
*QualityTestApi* | [**search_quality_schemas**](docs/QualityTestApi.md#search_quality_schemas) | **POST** /v2/quality_schema/search | Search quality schemas for a factory
*QualityTestApi* | [**search_quality_tests**](docs/QualityTestApi.md#search_quality_tests) | **POST** /v2/quality_test/search | Search quality tests
*QualityTestApi* | [**set_quality_test**](docs/QualityTestApi.md#set_quality_test) | **POST** /v2/quality_test/set | Create or update a quality test result
*ScrapYieldDataApi* | [**delete_scrap_yield**](docs/ScrapYieldDataApi.md#delete_scrap_yield) | **POST** /v2/scrap_yield/delete | Delete a scrap/yield record
*ScrapYieldDataApi* | [**search_scrap_yield**](docs/ScrapYieldDataApi.md#search_scrap_yield) | **POST** /v2/scrap_yield/search | Search scrap/yield records
*ScrapYieldDataApi* | [**set_scrap_yield**](docs/ScrapYieldDataApi.md#set_scrap_yield) | **POST** /v2/scrap_yield/set | Create or update a scrap/yield record
*TargetsApi* | [**search_targets**](docs/TargetsApi.md#search_targets) | **POST** /v2/target/search | Search metric targets
*TargetsApi* | [**set_target**](docs/TargetsApi.md#set_target) | **POST** /v2/target/set | Create or update a metric target


## Documentation For Models

 - [BatchMetadata](docs/BatchMetadata.md)
 - [CustomMetadata](docs/CustomMetadata.md)
 - [DashboardColumnSpec](docs/DashboardColumnSpec.md)
 - [DashboardExecuteFilters](docs/DashboardExecuteFilters.md)
 - [DashboardExecuteFiltersCustomIntervals](docs/DashboardExecuteFiltersCustomIntervals.md)
 - [DashboardExecuteFiltersStates](docs/DashboardExecuteFiltersStates.md)
 - [DashboardExecuteFiltersStatesStateCategoryAndReasons](docs/DashboardExecuteFiltersStatesStateCategoryAndReasons.md)
 - [DashboardExecuteRange](docs/DashboardExecuteRange.md)
 - [DashboardExecuteRequest](docs/DashboardExecuteRequest.md)
 - [DashboardExecuteRequestDashboard](docs/DashboardExecuteRequestDashboard.md)
 - [DashboardExecuteResult](docs/DashboardExecuteResult.md)
 - [DashboardExecuteResultRange](docs/DashboardExecuteResultRange.md)
 - [Factory](docs/Factory.md)
 - [GenericError](docs/GenericError.md)
 - [InlineObject](docs/InlineObject.md)
 - [InlineObject1](docs/InlineObject1.md)
 - [InlineObject2](docs/InlineObject2.md)
 - [InlineObject3](docs/InlineObject3.md)
 - [InlineObject4](docs/InlineObject4.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse200FailedIntervals](docs/InlineResponse200FailedIntervals.md)
 - [InlineResponse400](docs/InlineResponse400.md)
 - [InlineResponse409](docs/InlineResponse409.md)
 - [InlineResponse500](docs/InlineResponse500.md)
 - [Interval](docs/Interval.md)
 - [IntervalBulkCreate](docs/IntervalBulkCreate.md)
 - [IntervalBulkDelete](docs/IntervalBulkDelete.md)
 - [IntervalBulkUpdate](docs/IntervalBulkUpdate.md)
 - [IntervalType](docs/IntervalType.md)
 - [IntervalTypeSet](docs/IntervalTypeSet.md)
 - [Line](docs/Line.md)
 - [MaintenanceWorkOrder](docs/MaintenanceWorkOrder.md)
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


