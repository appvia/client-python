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
from swagger_client.models.version_version_kind import VersionVersionKind  # noqa: F401,E501


class PackageVersion(object):
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
        'epoch': 'int',
        'name': 'str',
        'revision': 'str',
        'kind': 'VersionVersionKind'
    }

    attribute_map = {
        'epoch': 'epoch',
        'name': 'name',
        'revision': 'revision',
        'kind': 'kind'
    }

    def __init__(self, epoch=None, name=None, revision=None, kind=None):  # noqa: E501
        """PackageVersion - a model defined in Swagger"""  # noqa: E501
        self._epoch = None
        self._name = None
        self._revision = None
        self._kind = None
        self.discriminator = None
        if epoch is not None:
            self.epoch = epoch
        if name is not None:
            self.name = name
        if revision is not None:
            self.revision = revision
        if kind is not None:
            self.kind = kind

    @property
    def epoch(self):
        """Gets the epoch of this PackageVersion.  # noqa: E501

        Used to correct mistakes in the version numbering scheme.  # noqa: E501

        :return: The epoch of this PackageVersion.  # noqa: E501
        :rtype: int
        """
        return self._epoch

    @epoch.setter
    def epoch(self, epoch):
        """Sets the epoch of this PackageVersion.

        Used to correct mistakes in the version numbering scheme.  # noqa: E501

        :param epoch: The epoch of this PackageVersion.  # noqa: E501
        :type: int
        """

        self._epoch = epoch

    @property
    def name(self):
        """Gets the name of this PackageVersion.  # noqa: E501

        Required only when version kind is NORMAL. The main part of the version name.  # noqa: E501

        :return: The name of this PackageVersion.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PackageVersion.

        Required only when version kind is NORMAL. The main part of the version name.  # noqa: E501

        :param name: The name of this PackageVersion.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def revision(self):
        """Gets the revision of this PackageVersion.  # noqa: E501

        The iteration of the package build from the above version.  # noqa: E501

        :return: The revision of this PackageVersion.  # noqa: E501
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this PackageVersion.

        The iteration of the package build from the above version.  # noqa: E501

        :param revision: The revision of this PackageVersion.  # noqa: E501
        :type: str
        """

        self._revision = revision

    @property
    def kind(self):
        """Gets the kind of this PackageVersion.  # noqa: E501


        :return: The kind of this PackageVersion.  # noqa: E501
        :rtype: VersionVersionKind
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this PackageVersion.


        :param kind: The kind of this PackageVersion.  # noqa: E501
        :type: VersionVersionKind
        """

        self._kind = kind

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
        if issubclass(PackageVersion, dict):
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
        if not isinstance(other, PackageVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
