# coding: utf-8

"""
    grafeas.proto

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: version not set
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.v1beta1_note_kind import V1beta1NoteKind  # noqa: F401,E501


class DiscoveryDiscovery(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'analysis_kind': 'V1beta1NoteKind'
    }

    attribute_map = {
        'analysis_kind': 'analysis_kind'
    }

    def __init__(self, analysis_kind=None):  # noqa: E501
        """DiscoveryDiscovery - a model defined in Swagger"""  # noqa: E501

        self._analysis_kind = None
        self.discriminator = None

        if analysis_kind is not None:
            self.analysis_kind = analysis_kind

    @property
    def analysis_kind(self):
        """Gets the analysis_kind of this DiscoveryDiscovery.  # noqa: E501

        Required. Immutable. The kind of analysis that is handled by this discovery.  # noqa: E501

        :return: The analysis_kind of this DiscoveryDiscovery.  # noqa: E501
        :rtype: V1beta1NoteKind
        """
        return self._analysis_kind

    @analysis_kind.setter
    def analysis_kind(self, analysis_kind):
        """Sets the analysis_kind of this DiscoveryDiscovery.

        Required. Immutable. The kind of analysis that is handled by this discovery.  # noqa: E501

        :param analysis_kind: The analysis_kind of this DiscoveryDiscovery.  # noqa: E501
        :type: V1beta1NoteKind
        """

        self._analysis_kind = analysis_kind

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(DiscoveryDiscovery, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DiscoveryDiscovery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
