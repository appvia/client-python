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

from swagger_client.models.v1beta1_occurrence import V1beta1Occurrence  # noqa: F401,E501


class V1beta1BatchCreateOccurrencesRequest(object):
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
        'parent': 'str',
        'occurrences': 'list[V1beta1Occurrence]'
    }

    attribute_map = {
        'parent': 'parent',
        'occurrences': 'occurrences'
    }

    def __init__(self, parent=None, occurrences=None):  # noqa: E501
        """V1beta1BatchCreateOccurrencesRequest - a model defined in Swagger"""  # noqa: E501

        self._parent = None
        self._occurrences = None
        self.discriminator = None

        if parent is not None:
            self.parent = parent
        if occurrences is not None:
            self.occurrences = occurrences

    @property
    def parent(self):
        """Gets the parent of this V1beta1BatchCreateOccurrencesRequest.  # noqa: E501

        The name of the project in the form of `projects/[PROJECT_ID]`, under which the occurrences are to be created.  # noqa: E501

        :return: The parent of this V1beta1BatchCreateOccurrencesRequest.  # noqa: E501
        :rtype: str
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this V1beta1BatchCreateOccurrencesRequest.

        The name of the project in the form of `projects/[PROJECT_ID]`, under which the occurrences are to be created.  # noqa: E501

        :param parent: The parent of this V1beta1BatchCreateOccurrencesRequest.  # noqa: E501
        :type: str
        """

        self._parent = parent

    @property
    def occurrences(self):
        """Gets the occurrences of this V1beta1BatchCreateOccurrencesRequest.  # noqa: E501

        The occurrences to create. Max allowed length is 1000.  # noqa: E501

        :return: The occurrences of this V1beta1BatchCreateOccurrencesRequest.  # noqa: E501
        :rtype: list[V1beta1Occurrence]
        """
        return self._occurrences

    @occurrences.setter
    def occurrences(self, occurrences):
        """Sets the occurrences of this V1beta1BatchCreateOccurrencesRequest.

        The occurrences to create. Max allowed length is 1000.  # noqa: E501

        :param occurrences: The occurrences of this V1beta1BatchCreateOccurrencesRequest.  # noqa: E501
        :type: list[V1beta1Occurrence]
        """

        self._occurrences = occurrences

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
        if issubclass(V1beta1BatchCreateOccurrencesRequest, dict):
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
        if not isinstance(other, V1beta1BatchCreateOccurrencesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other