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
from swagger_client.models.source_repo_id import SourceRepoId  # noqa: F401,E501


class SourceCloudRepoSourceContext(object):
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
        'repo_id': 'SourceRepoId',
        'revision_id': 'str',
        'alias_context': 'SourceAliasContext'
    }

    attribute_map = {
        'repo_id': 'repo_id',
        'revision_id': 'revision_id',
        'alias_context': 'alias_context'
    }

    def __init__(self, repo_id=None, revision_id=None, alias_context=None):  # noqa: E501
        """SourceCloudRepoSourceContext - a model defined in Swagger"""  # noqa: E501

        self._repo_id = None
        self._revision_id = None
        self._alias_context = None
        self.discriminator = None

        if repo_id is not None:
            self.repo_id = repo_id
        if revision_id is not None:
            self.revision_id = revision_id
        if alias_context is not None:
            self.alias_context = alias_context

    @property
    def repo_id(self):
        """Gets the repo_id of this SourceCloudRepoSourceContext.  # noqa: E501

        The ID of the repo.  # noqa: E501

        :return: The repo_id of this SourceCloudRepoSourceContext.  # noqa: E501
        :rtype: SourceRepoId
        """
        return self._repo_id

    @repo_id.setter
    def repo_id(self, repo_id):
        """Sets the repo_id of this SourceCloudRepoSourceContext.

        The ID of the repo.  # noqa: E501

        :param repo_id: The repo_id of this SourceCloudRepoSourceContext.  # noqa: E501
        :type: SourceRepoId
        """

        self._repo_id = repo_id

    @property
    def revision_id(self):
        """Gets the revision_id of this SourceCloudRepoSourceContext.  # noqa: E501

        A revision ID.  # noqa: E501

        :return: The revision_id of this SourceCloudRepoSourceContext.  # noqa: E501
        :rtype: str
        """
        return self._revision_id

    @revision_id.setter
    def revision_id(self, revision_id):
        """Sets the revision_id of this SourceCloudRepoSourceContext.

        A revision ID.  # noqa: E501

        :param revision_id: The revision_id of this SourceCloudRepoSourceContext.  # noqa: E501
        :type: str
        """

        self._revision_id = revision_id

    @property
    def alias_context(self):
        """Gets the alias_context of this SourceCloudRepoSourceContext.  # noqa: E501

        An alias, which may be a branch or tag.  # noqa: E501

        :return: The alias_context of this SourceCloudRepoSourceContext.  # noqa: E501
        :rtype: SourceAliasContext
        """
        return self._alias_context

    @alias_context.setter
    def alias_context(self, alias_context):
        """Sets the alias_context of this SourceCloudRepoSourceContext.

        An alias, which may be a branch or tag.  # noqa: E501

        :param alias_context: The alias_context of this SourceCloudRepoSourceContext.  # noqa: E501
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
        if issubclass(SourceCloudRepoSourceContext, dict):
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
        if not isinstance(other, SourceCloudRepoSourceContext):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other