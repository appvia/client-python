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

from swagger_client.models.source_alias_context import SourceAliasContext  # noqa: F401,E501


class SourceGerritSourceContext(object):
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
        'host_uri': 'str',
        'gerrit_project': 'str',
        'revision_id': 'str',
        'alias_context': 'SourceAliasContext'
    }

    attribute_map = {
        'host_uri': 'host_uri',
        'gerrit_project': 'gerrit_project',
        'revision_id': 'revision_id',
        'alias_context': 'alias_context'
    }

    def __init__(self, host_uri=None, gerrit_project=None, revision_id=None, alias_context=None):  # noqa: E501
        """SourceGerritSourceContext - a model defined in Swagger"""  # noqa: E501

        self._host_uri = None
        self._gerrit_project = None
        self._revision_id = None
        self._alias_context = None
        self.discriminator = None

        if host_uri is not None:
            self.host_uri = host_uri
        if gerrit_project is not None:
            self.gerrit_project = gerrit_project
        if revision_id is not None:
            self.revision_id = revision_id
        if alias_context is not None:
            self.alias_context = alias_context

    @property
    def host_uri(self):
        """Gets the host_uri of this SourceGerritSourceContext.  # noqa: E501

        The URI of a running Gerrit instance.  # noqa: E501

        :return: The host_uri of this SourceGerritSourceContext.  # noqa: E501
        :rtype: str
        """
        return self._host_uri

    @host_uri.setter
    def host_uri(self, host_uri):
        """Sets the host_uri of this SourceGerritSourceContext.

        The URI of a running Gerrit instance.  # noqa: E501

        :param host_uri: The host_uri of this SourceGerritSourceContext.  # noqa: E501
        :type: str
        """

        self._host_uri = host_uri

    @property
    def gerrit_project(self):
        """Gets the gerrit_project of this SourceGerritSourceContext.  # noqa: E501

        The full project name within the host. Projects may be nested, so \"project/subproject\" is a valid project name. The \"repo name\" is the hostURI/project.  # noqa: E501

        :return: The gerrit_project of this SourceGerritSourceContext.  # noqa: E501
        :rtype: str
        """
        return self._gerrit_project

    @gerrit_project.setter
    def gerrit_project(self, gerrit_project):
        """Sets the gerrit_project of this SourceGerritSourceContext.

        The full project name within the host. Projects may be nested, so \"project/subproject\" is a valid project name. The \"repo name\" is the hostURI/project.  # noqa: E501

        :param gerrit_project: The gerrit_project of this SourceGerritSourceContext.  # noqa: E501
        :type: str
        """

        self._gerrit_project = gerrit_project

    @property
    def revision_id(self):
        """Gets the revision_id of this SourceGerritSourceContext.  # noqa: E501

        A revision (commit) ID.  # noqa: E501

        :return: The revision_id of this SourceGerritSourceContext.  # noqa: E501
        :rtype: str
        """
        return self._revision_id

    @revision_id.setter
    def revision_id(self, revision_id):
        """Sets the revision_id of this SourceGerritSourceContext.

        A revision (commit) ID.  # noqa: E501

        :param revision_id: The revision_id of this SourceGerritSourceContext.  # noqa: E501
        :type: str
        """

        self._revision_id = revision_id

    @property
    def alias_context(self):
        """Gets the alias_context of this SourceGerritSourceContext.  # noqa: E501

        An alias, which may be a branch or tag.  # noqa: E501

        :return: The alias_context of this SourceGerritSourceContext.  # noqa: E501
        :rtype: SourceAliasContext
        """
        return self._alias_context

    @alias_context.setter
    def alias_context(self, alias_context):
        """Sets the alias_context of this SourceGerritSourceContext.

        An alias, which may be a branch or tag.  # noqa: E501

        :param alias_context: The alias_context of this SourceGerritSourceContext.  # noqa: E501
        :type: SourceAliasContext
        """

        self._alias_context = alias_context

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
        if issubclass(SourceGerritSourceContext, dict):
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
        if not isinstance(other, SourceGerritSourceContext):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other