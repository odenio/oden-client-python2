# coding: utf-8

"""
    Oden API

    The Oden Private Partner API exposes RESTful API endpoints for clients to get, create and update data on the Oden Platform.  The API is based on the OpenAPI 3.0 specification. ### Current Version The URL, and host, for the current version is [https://api.oden.app/v2](https://api.oden.app/v2).  ### Oden's Data Model - **Organization**: This represents the Organization registered as an Oden customer. An organization has an associated collection of users, factories, lines, etc. This is the entity a specific authentication token is associated with. - **Asset** or **Machinegroup**: Assets, or machinegroups, are collections of machines, which may either be a **Factory** or a **Line**:   - **Factory**: Factories are collections of lines, representing a particular manufacturing location.     - **Line**: Lines are collections of machines, often representing a particular production line. Lines may also have **Products** mapped to them, indicating what is currently being manufactured by the specific line.       - **Machine**: Machines are the physical machines that make up a line - **Product**: Products capture what entities a manufacturer produces - **Interval**: An interval is a period of time that takes place on a manufacturing line and expresses some business concern. It's Oden's way of making metrics aggregatable, traceable, and relatable to a manufacturer.   - **Run**: A run is a production interval that labels a period of production as being work on some single product   - **Batch**: A batch is a production interval that represents a portion of a particular run   - **State**: A state is an interval that tracks the availability or utilization of a line     - **State Category**: A state category describes what state a line is in - such as ex. uptime, downtime, scrapping, etc.     - **State Reason**: A state reason describes why a line is in a particular state - such as \"maintenance\" being a reason for the category \"downtime\".   - **Custom**: A custom interval can track any other type of interval-based data a manufacturer might want to analyze. These are created on a per-factory basis. - **Target**: Targets specify values and upper/lower thresholds for metrics when specific products are running on specific lines - **Scrap/Yield**: Scrap/yield output specifies amount of produced product on a line during either a run or batch interval. Oden will categorize all output as either scrap or yield - as specified by the Scrap Yield Schema for a given factory. If you have other categories, like rework/blocked/off-grade, you must choose between categorizing those amounts as either good or bad production by specifying as scrap or yield. Clients may also add scrap codes (i.e., reasons) to a given Scrap Yield Data entry.   - **Scrap Code**: A scrap code is a code that explains the reason for a scrap/yield raw data input - such as \"Rework\" - **Quality Test**: Quality Tests are results of quality assurance tests done on site, and uploaded to Oden. They may be attached to a single Batch or Run. - **Metric**: Known in factories as \"tags\", metrics are the raw data that is collected by Oden from the machines and devices on the factory floor. - **Metric Group**: Metric groups are metrics that represent the same thing across different lines. They provide common display names for tags and allow labeling groups of tags as measuring key types of data like performance or production.  ### Best Practices Under the current implementation, the Oden API does not rate limit requests from clients.  However, rate limiting will be introduced in the near future and it is recommended that users design their API clients to not exceed a request rate of **one per second**.  ### Schema All v2 API access is over HTTPS and accessed from https://api.oden.app/v2 All data is sent and received as JSON.  API requests with duplicate keys will process only the data for the first key detected and ignore the rest, so it's not recommended. Batching multiple messages in this way is currently not possible.   - Example of duplicate key in JSON: {\"raw_data\":{\"scrap\":\"10\",\"scrap\":\"100\"}}  All timestamps are returned in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#Times) format:    `YYYY-MM-DDTHH:MM:SSZ`  All durations are returned in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#Times) format with the largest unit of time being the hour:     `PT[n]H[n]M[n]S`  All timestamps sent to the API in POST requests should be in ISO 8601 format. ### HTTP Verbs The ONLY HTTP call type (sometimes called *verb* or *method*) used within Oden's API is **POST**. There are three actions supported via a **POST**; call, search, set, and delete, together supporting CRUD operations;   - **search** requests are used to search for and *read* objects in the Oden Platform       - All Oden Objects may be uniquely identified by some combination of, or a single, parameter.         - Ex a `line` my be identified by either:           - `id`           - `name` AND `factory`   - **set** requests are used to *create* or *update* objects   - **delete** requests are used to *delete* objects. If a delete endpoint is not yet implemented for a given object, users may choose to update the values of a specific entity to null or 0 values.  ### URI Components All endpoints may be accessed with the URI pattern: `https://api.oden.app/v2/{object}/{action}`  Where:   - `object` is the name of the object being requested:        - `factory`, `quality_test`, `interval`, `line`, etc...   - `action` is the name of the action being requested     - `search` , `set` , `delete`  e.g. `https://api.oden.app/v2/factory/search`  # Authentication Clients can authenticate through the v2 API using a Token provided by Oden. Tokens are opaque strings similar to [Bearer](https://swagger.io/docs/specification/authentication/bearer-authentication/) tokens that the client must pass in the [HTTP Authorization request header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization) in every request. The syntax is as follows:  `Authorization: <type> <credentials>`  Where \\<type\\> is \"Token\" and \\<credentials\\> is the Token string. For example:  `Authorization: Token tokenStringProvidedByOden`  Authenticating with an invalid Token will return `401 Unauthorized Error`.  Authenticating with a Token that is not authorized to read requested data will return `403 Forbidden Error`.  Some endpoints may require requests to be broken out by machinegroup (i.e., line or factory) and the number of requests would scale accordingly. This multiplicity should be taken into consideration when deciding on the frequency the API client makes requests to the Oden endpoints.  To authenticate in this [UI](https://api.oden.app/v2/ui/), click the Lock icon, and copy/paste the token into the Authorize box.   # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: support@oden.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from oden.api_client import ApiClient
from oden.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class IntervalsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v2_interval_delete_post(self, interval, **kwargs):  # noqa: E501
        """v2_interval_delete_post  # noqa: E501

        Delete an interval by `type`, `line`, and `id`  **Note:** The `id` must be obtained from either: - The response when creating an interval via `/v2/interval/set` - Searching for intervals via `/v2/interval/search`  The examples below use placeholder IDs - replace with actual IDs from your system.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_interval_delete_post(interval, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param Interval interval: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[Interval]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.v2_interval_delete_post_with_http_info(interval, **kwargs)  # noqa: E501

    def v2_interval_delete_post_with_http_info(self, interval, **kwargs):  # noqa: E501
        """v2_interval_delete_post  # noqa: E501

        Delete an interval by `type`, `line`, and `id`  **Note:** The `id` must be obtained from either: - The response when creating an interval via `/v2/interval/set` - Searching for intervals via `/v2/interval/search`  The examples below use placeholder IDs - replace with actual IDs from your system.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_interval_delete_post_with_http_info(interval, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param Interval interval: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[Interval], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'interval'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_interval_delete_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'interval' is set
        if self.api_client.client_side_validation and ('interval' not in local_var_params or  # noqa: E501
                                                        local_var_params['interval'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `interval` when calling `v2_interval_delete_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'interval' in local_var_params:
            body_params = local_var_params['interval']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v2/interval/delete', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Interval]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v2_interval_search_post(self, interval, **kwargs):  # noqa: E501
        """v2_interval_search_post  # noqa: E501

        Searches for intervals by `type`, `line` and other optional parameters:  - `id` (for a specific Interval) - `match: unique` or omit  OR  - `match : last` for the most recent Interval of the given type on the given line  OR  - `start_time` and `end_time` (for a range of Intervals over a period of time) - `match: all` for more than one result  OR  - match all intervals for all lines in a given factory  AND/OR  - `name` (only for Intervals with a matching name)   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_interval_search_post(interval, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param Interval interval: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[Interval]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.v2_interval_search_post_with_http_info(interval, **kwargs)  # noqa: E501

    def v2_interval_search_post_with_http_info(self, interval, **kwargs):  # noqa: E501
        """v2_interval_search_post  # noqa: E501

        Searches for intervals by `type`, `line` and other optional parameters:  - `id` (for a specific Interval) - `match: unique` or omit  OR  - `match : last` for the most recent Interval of the given type on the given line  OR  - `start_time` and `end_time` (for a range of Intervals over a period of time) - `match: all` for more than one result  OR  - match all intervals for all lines in a given factory  AND/OR  - `name` (only for Intervals with a matching name)   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_interval_search_post_with_http_info(interval, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param Interval interval: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[Interval], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'interval'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_interval_search_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'interval' is set
        if self.api_client.client_side_validation and ('interval' not in local_var_params or  # noqa: E501
                                                        local_var_params['interval'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `interval` when calling `v2_interval_search_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'interval' in local_var_params:
            body_params = local_var_params['interval']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v2/interval/search', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Interval]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v2_interval_set_post(self, interval, **kwargs):  # noqa: E501
        """v2_interval_set_post  # noqa: E501

        Create or update an Interval.  Must include `line` and `type`. `match` must be omitted, `unique` or `last`   - If `id` is not supplied, a new Interval will be created.   - If `id` is supplied, existing Interval will be updated. This interval's start time can be modified using `start_time` field.  To update a specific interval supply the `id` of that interval.  If the interval exists with all the same parameters nothing is done.  To update the most recent Interval of a given `type` on a `line` one may use `match: last` and omit `id`  For `RUN` type: if `product` and/or `product_mapping` does not exist a new one will be created. Further a `target` may be set by adding a `target` to the metadata field. The `line` and `product` for this target will be the same as the interval.  Please see examples for more specific information.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_interval_set_post(interval, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param Interval interval: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[Interval]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.v2_interval_set_post_with_http_info(interval, **kwargs)  # noqa: E501

    def v2_interval_set_post_with_http_info(self, interval, **kwargs):  # noqa: E501
        """v2_interval_set_post  # noqa: E501

        Create or update an Interval.  Must include `line` and `type`. `match` must be omitted, `unique` or `last`   - If `id` is not supplied, a new Interval will be created.   - If `id` is supplied, existing Interval will be updated. This interval's start time can be modified using `start_time` field.  To update a specific interval supply the `id` of that interval.  If the interval exists with all the same parameters nothing is done.  To update the most recent Interval of a given `type` on a `line` one may use `match: last` and omit `id`  For `RUN` type: if `product` and/or `product_mapping` does not exist a new one will be created. Further a `target` may be set by adding a `target` to the metadata field. The `line` and `product` for this target will be the same as the interval.  Please see examples for more specific information.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_interval_set_post_with_http_info(interval, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param Interval interval: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[Interval], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'interval'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_interval_set_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'interval' is set
        if self.api_client.client_side_validation and ('interval' not in local_var_params or  # noqa: E501
                                                        local_var_params['interval'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `interval` when calling `v2_interval_set_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'interval' in local_var_params:
            body_params = local_var_params['interval']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v2/interval/set', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Interval]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v2_interval_type_search_post(self, interval_type, **kwargs):  # noqa: E501
        """v2_interval_type_search_post  # noqa: E501

        Search for Interval Types by `name`, `id`, `factory` or just `match: all` to return all Interval Types associated with the your organization. Basic Interval Types -- `RUN`, `BATCH`, and `STATE` -- are associated with every factory in Oden's system. Custom Interval Types may be created by users, are set on a per factory basis, and may only describe Intervals on Lines associated with that Factory.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_interval_type_search_post(interval_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param IntervalType interval_type: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[IntervalType]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.v2_interval_type_search_post_with_http_info(interval_type, **kwargs)  # noqa: E501

    def v2_interval_type_search_post_with_http_info(self, interval_type, **kwargs):  # noqa: E501
        """v2_interval_type_search_post  # noqa: E501

        Search for Interval Types by `name`, `id`, `factory` or just `match: all` to return all Interval Types associated with the your organization. Basic Interval Types -- `RUN`, `BATCH`, and `STATE` -- are associated with every factory in Oden's system. Custom Interval Types may be created by users, are set on a per factory basis, and may only describe Intervals on Lines associated with that Factory.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_interval_type_search_post_with_http_info(interval_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param IntervalType interval_type: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[IntervalType], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'interval_type'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_interval_type_search_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'interval_type' is set
        if self.api_client.client_side_validation and ('interval_type' not in local_var_params or  # noqa: E501
                                                        local_var_params['interval_type'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `interval_type` when calling `v2_interval_type_search_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'interval_type' in local_var_params:
            body_params = local_var_params['interval_type']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v2/interval_type/search', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[IntervalType]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v2_intervals_delete_post(self, interval_bulk_delete, **kwargs):  # noqa: E501
        """v2_intervals_delete_post  # noqa: E501

        Delete a group of intervals by a single `type` and a single `line`, between `start_time` and `end_time`. Returns a list of intervals that were not deleted, and the number of intervals deleted.  Limitations: - Cannot exceed 15,000 intervals per request, or 30 days worth of data. - Currently does not support \"batch\" or \"run\" interval types.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_intervals_delete_post(interval_bulk_delete, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param IntervalBulkDelete interval_bulk_delete: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.v2_intervals_delete_post_with_http_info(interval_bulk_delete, **kwargs)  # noqa: E501

    def v2_intervals_delete_post_with_http_info(self, interval_bulk_delete, **kwargs):  # noqa: E501
        """v2_intervals_delete_post  # noqa: E501

        Delete a group of intervals by a single `type` and a single `line`, between `start_time` and `end_time`. Returns a list of intervals that were not deleted, and the number of intervals deleted.  Limitations: - Cannot exceed 15,000 intervals per request, or 30 days worth of data. - Currently does not support \"batch\" or \"run\" interval types.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_intervals_delete_post_with_http_info(interval_bulk_delete, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param IntervalBulkDelete interval_bulk_delete: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(InlineResponse2001, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'interval_bulk_delete'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_intervals_delete_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'interval_bulk_delete' is set
        if self.api_client.client_side_validation and ('interval_bulk_delete' not in local_var_params or  # noqa: E501
                                                        local_var_params['interval_bulk_delete'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `interval_bulk_delete` when calling `v2_intervals_delete_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'interval_bulk_delete' in local_var_params:
            body_params = local_var_params['interval_bulk_delete']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v2/intervals/delete', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2001',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v2_intervals_set_post(self, interval_bulk_create, **kwargs):  # noqa: E501
        """v2_intervals_set_post  # noqa: E501

        Create (Does not update) a group of custom intervals, for the same `type` and `line`. Line and type do not need to be included in each individual interval, just once at the top level.  Limitations: - Cannot excees 2500 intervals per request. - Will not write over other intervals - Does not support \"batch\", \"run\", or \"state\" interval types.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_intervals_set_post(interval_bulk_create, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param IntervalBulkCreate interval_bulk_create: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.v2_intervals_set_post_with_http_info(interval_bulk_create, **kwargs)  # noqa: E501

    def v2_intervals_set_post_with_http_info(self, interval_bulk_create, **kwargs):  # noqa: E501
        """v2_intervals_set_post  # noqa: E501

        Create (Does not update) a group of custom intervals, for the same `type` and `line`. Line and type do not need to be included in each individual interval, just once at the top level.  Limitations: - Cannot excees 2500 intervals per request. - Will not write over other intervals - Does not support \"batch\", \"run\", or \"state\" interval types.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_intervals_set_post_with_http_info(interval_bulk_create, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param IntervalBulkCreate interval_bulk_create: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(InlineResponse200, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'interval_bulk_create'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_intervals_set_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'interval_bulk_create' is set
        if self.api_client.client_side_validation and ('interval_bulk_create' not in local_var_params or  # noqa: E501
                                                        local_var_params['interval_bulk_create'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `interval_bulk_create` when calling `v2_intervals_set_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'interval_bulk_create' in local_var_params:
            body_params = local_var_params['interval_bulk_create']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v2/intervals/set', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
