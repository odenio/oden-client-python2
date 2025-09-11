# coding: utf-8

"""
    Oden API

    The Oden Private Partner API exposes RESTful API endpoints for clients to get, create and update data on the Oden Platform.  The API is based on the OpenAPI 3.0 specification. ### Current Version The URL, and host, for the current version is [https://api.oden.app/v2](https://api.oden.app/v2).  ### Oden's Data Model - **Organization**: This represents the Organization registered as an Oden customer. An organization has an associated collection of users, factories, lines, etc. This is the entity a specific authentication token is associated with. - **Asset** or **Machinegroup**: Assets, or machinegroups, are collections of machines, which may either be a **Factory** or a **Line**:   - **Factory**: Factories are collections of lines, representing a particular manufacturing location.     - **Line**: Lines are collections of machines, often representing a particular production line. Lines may also have **Products** mapped to them, indicating what is currently being manufactured by the specific line.       - **Machine**: Machines are the physical machines that make up a line - **Product**: Products capture what entities a manufacturer produces - **Interval**: An interval is a period of time that takes place on a manufacturing line and expresses some business concern. It's Oden's way of making metrics aggregatable, traceable, and relatable to a manufacturer.   - **Run**: A run is a production interval that labels a period of production as being work on some single product   - **Batch**: A batch is a production interval that represents a portion of a particular run   - **State**: A state is an interval that tracks the availability or utilization of a line     - **State Category**: A state category describes what state a line is in - such as ex. uptime, downtime, scrapping, etc.     - **State Reason**: A state reason describes why a line is in a particular state - such as \"maintenance\" being a reason for the category \"downtime\".   - **Custom**: A custom interval can track any other type of interval-based data a manufacturer might want to analyze. These are created on a per-factory basis. - **Target**: Targets specify values and upper/lower thresholds for metrics when specific products are running on specific lines - **Scrap/Yield**: Scrap/yield output specifies amount of produced product on a line during either a run or batch interval. Oden will categorize all output as either scrap or yield - as specified by the Scrap Yield Schema for a given factory. If you have other categories, like rework/blocked/off-grade, you must choose between categorizing those amounts as either good or bad production by specifying as scrap or yield. Clients may also add scrap codes (i.e., reasons) to a given Scrap Yield Data entry.   - **Scrap Code**: A scrap code is a code that explains the reason for a scrap/yield raw data input - such as \"Rework\" - **Quality Test**: Quality Tests are results of quality assurance tests done on site, and uploaded to Oden. They may be attached to a single Batch or Run. - **Metric**: Known in factories as \"tags\", metrics are the raw data that is collected by Oden from the machines and devices on the factory floor. - **Metric Group**: Metric groups are metrics that represent the same thing across different lines. They provide common display names for tags and allow labeling groups of tags as measuring key types of data like performance or production.  ### Best Practices Under the current implementation, the Oden API does not rate limit requests from clients.  However, rate limiting will be introduced in the near future and it is recommended that users design their API clients to not exceed a request rate of **one per second**.  ### Schema All v2 API access is over HTTPS and accessed from https://api.oden.app/v2 All data is sent and received as JSON.  API requests with duplicate keys will process only the data for the first key detected and ignore the rest, so it's not recommended. Batching multiple messages in this way is currently not possible.   - Example of duplicate key in JSON: {\"raw_data\":{\"scrap\":\"10\",\"scrap\":\"100\"}}  All timestamps are returned in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#Times) format:    `YYYY-MM-DDTHH:MM:SSZ`  All durations are returned in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#Times) format with the largest unit of time being the hour:     `PT[n]H[n]M[n]S`  All timestamps sent to the API in POST requests should be in ISO 8601 format. ### HTTP Verbs The ONLY HTTP call type (sometimes called *verb* or *method*) used within Oden's API is **POST**. There are three actions supported via a **POST**; call, search, set, and delete, together supporting CRUD operations;   - **search** requests are used to search for and *read* objects in the Oden Platform       - All Oden Objects may be uniquely identified by some combination of, or a single, parameter.         - Ex a `line` my be identified by either:           - `id`           - `name` AND `factory`   - **set** requests are used to *create* or *update* objects   - **delete** requests are used to *delete* objects. If a delete endpoint is not yet implemented for a given object, users may choose to update the values of a specific entity to null or 0 values.  ### URI Components All endpoints may be accessed with the URI pattern: `https://api.oden.app/v2/{object}/{action}`  Where:   - `object` is the name of the object being requested:        - `factory`, `quality_test`, `interval`, `line`, etc...   - `action` is the name of the action being requested     - `search` , `set` , `delete`  e.g. `https://api.oden.app/v2/factory/search`  # Authentication Clients can authenticate through the v2 API using a Token provided by Oden. Tokens are opaque strings similar to [Bearer](https://swagger.io/docs/specification/authentication/bearer-authentication/) tokens that the client must pass in the [HTTP Authorization request header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization) in every request. The syntax is as follows:  `Authorization: <type> <credentials>`  Where \\<type\\> is \"Token\" and \\<credentials\\> is the Token string. For example:  `Authorization: Token tokenStringProvidedByOden`  Authenticating with an invalid Token will return `401 Unauthorized Error`.  Authenticating with a Token that is not authorized to read requested data will return `403 Forbidden Error`.  Some endpoints may require requests to be broken out by machinegroup (i.e., line or factory) and the number of requests would scale accordingly. This multiplicity should be taken into consideration when deciding on the frequency the API client makes requests to the Oden endpoints.  To authenticate in this [UI](https://api.oden.app/v2/ui/), click the Lock icon, and copy/paste the token into the Authorize box.   # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: support@oden.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from oden.configuration import Configuration


class ScrapYieldSchema(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'str',
        'factory': 'Factory',
        'scrap_conversion_factor': 'float',
        'scrap_unit': 'Unit',
        'yield_conversion_factor': 'float',
        'yield_unit': 'Unit'
    }

    attribute_map = {
        'id': 'id',
        'factory': 'factory',
        'scrap_conversion_factor': 'scrap_conversion_factor',
        'scrap_unit': 'scrap_unit',
        'yield_conversion_factor': 'yield_conversion_factor',
        'yield_unit': 'yield_unit'
    }

    def __init__(self, id=None, factory=None, scrap_conversion_factor=None, scrap_unit=None, yield_conversion_factor=None, yield_unit=None, local_vars_configuration=None):  # noqa: E501
        """ScrapYieldSchema - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._factory = None
        self._scrap_conversion_factor = None
        self._scrap_unit = None
        self._yield_conversion_factor = None
        self._yield_unit = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if factory is not None:
            self.factory = factory
        if scrap_conversion_factor is not None:
            self.scrap_conversion_factor = scrap_conversion_factor
        if scrap_unit is not None:
            self.scrap_unit = scrap_unit
        if yield_conversion_factor is not None:
            self.yield_conversion_factor = yield_conversion_factor
        if yield_unit is not None:
            self.yield_unit = yield_unit

    @property
    def id(self):
        """Gets the id of this ScrapYieldSchema.  # noqa: E501


        :return: The id of this ScrapYieldSchema.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ScrapYieldSchema.


        :param id: The id of this ScrapYieldSchema.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def factory(self):
        """Gets the factory of this ScrapYieldSchema.  # noqa: E501


        :return: The factory of this ScrapYieldSchema.  # noqa: E501
        :rtype: Factory
        """
        return self._factory

    @factory.setter
    def factory(self, factory):
        """Sets the factory of this ScrapYieldSchema.


        :param factory: The factory of this ScrapYieldSchema.  # noqa: E501
        :type: Factory
        """

        self._factory = factory

    @property
    def scrap_conversion_factor(self):
        """Gets the scrap_conversion_factor of this ScrapYieldSchema.  # noqa: E501


        :return: The scrap_conversion_factor of this ScrapYieldSchema.  # noqa: E501
        :rtype: float
        """
        return self._scrap_conversion_factor

    @scrap_conversion_factor.setter
    def scrap_conversion_factor(self, scrap_conversion_factor):
        """Sets the scrap_conversion_factor of this ScrapYieldSchema.


        :param scrap_conversion_factor: The scrap_conversion_factor of this ScrapYieldSchema.  # noqa: E501
        :type: float
        """

        self._scrap_conversion_factor = scrap_conversion_factor

    @property
    def scrap_unit(self):
        """Gets the scrap_unit of this ScrapYieldSchema.  # noqa: E501


        :return: The scrap_unit of this ScrapYieldSchema.  # noqa: E501
        :rtype: Unit
        """
        return self._scrap_unit

    @scrap_unit.setter
    def scrap_unit(self, scrap_unit):
        """Sets the scrap_unit of this ScrapYieldSchema.


        :param scrap_unit: The scrap_unit of this ScrapYieldSchema.  # noqa: E501
        :type: Unit
        """

        self._scrap_unit = scrap_unit

    @property
    def yield_conversion_factor(self):
        """Gets the yield_conversion_factor of this ScrapYieldSchema.  # noqa: E501


        :return: The yield_conversion_factor of this ScrapYieldSchema.  # noqa: E501
        :rtype: float
        """
        return self._yield_conversion_factor

    @yield_conversion_factor.setter
    def yield_conversion_factor(self, yield_conversion_factor):
        """Sets the yield_conversion_factor of this ScrapYieldSchema.


        :param yield_conversion_factor: The yield_conversion_factor of this ScrapYieldSchema.  # noqa: E501
        :type: float
        """

        self._yield_conversion_factor = yield_conversion_factor

    @property
    def yield_unit(self):
        """Gets the yield_unit of this ScrapYieldSchema.  # noqa: E501


        :return: The yield_unit of this ScrapYieldSchema.  # noqa: E501
        :rtype: Unit
        """
        return self._yield_unit

    @yield_unit.setter
    def yield_unit(self, yield_unit):
        """Sets the yield_unit of this ScrapYieldSchema.


        :param yield_unit: The yield_unit of this ScrapYieldSchema.  # noqa: E501
        :type: Unit
        """

        self._yield_unit = yield_unit

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ScrapYieldSchema):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScrapYieldSchema):
            return True

        return self.to_dict() != other.to_dict()
