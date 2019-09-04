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

from swagger_client.models.source_cloud_repo_source_context import SourceCloudRepoSourceContext  # noqa: F401,E501
from swagger_client.models.source_gerrit_source_context import SourceGerritSourceContext  # noqa: F401,E501
from swagger_client.models.source_git_source_context import SourceGitSourceContext  # noqa: F401,E501


class SourceSourceContext(object):
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
        'cloud_repo': 'SourceCloudRepoSourceContext',
        'gerrit': 'SourceGerritSourceContext',
        'git': 'SourceGitSourceContext',
        'labels': 'dict(str, str)'
    }

    attribute_map = {
        'cloud_repo': 'cloud_repo',
        'gerrit': 'gerrit',
        'git': 'git',
        'labels': 'labels'
    }

    def __init__(self, cloud_repo=None, gerrit=None, git=None, labels=None):  # noqa: E501
        """SourceSourceContext - a model defined in Swagger"""  # noqa: E501

        self._cloud_repo = None
        self._gerrit = None
        self._git = None
        self._labels = None
        self.discriminator = None

        if cloud_repo is not None:
            self.cloud_repo = cloud_repo
        if gerrit is not None:
            self.gerrit = gerrit
        if git is not None:
            self.git = git
        if labels is not None:
            self.labels = labels

    @property
    def cloud_repo(self):
        """Gets the cloud_repo of this SourceSourceContext.  # noqa: E501

        A SourceContext referring to a revision in a Google Cloud Source Repo.  # noqa: E501

        :return: The cloud_repo of this SourceSourceContext.  # noqa: E501
        :rtype: SourceCloudRepoSourceContext
        """
        return self._cloud_repo

    @cloud_repo.setter
    def cloud_repo(self, cloud_repo):
        """Sets the cloud_repo of this SourceSourceContext.

        A SourceContext referring to a revision in a Google Cloud Source Repo.  # noqa: E501

        :param cloud_repo: The cloud_repo of this SourceSourceContext.  # noqa: E501
        :type: SourceCloudRepoSourceContext
        """

        self._cloud_repo = cloud_repo

    @property
    def gerrit(self):
        """Gets the gerrit of this SourceSourceContext.  # noqa: E501

        A SourceContext referring to a Gerrit project.  # noqa: E501

        :return: The gerrit of this SourceSourceContext.  # noqa: E501
        :rtype: SourceGerritSourceContext
        """
        return self._gerrit

    @gerrit.setter
    def gerrit(self, gerrit):
        """Sets the gerrit of this SourceSourceContext.

        A SourceContext referring to a Gerrit project.  # noqa: E501

        :param gerrit: The gerrit of this SourceSourceContext.  # noqa: E501
        :type: SourceGerritSourceContext
        """

        self._gerrit = gerrit

    @property
    def git(self):
        """Gets the git of this SourceSourceContext.  # noqa: E501

        A SourceContext referring to any third party Git repo (e.g., GitHub).  # noqa: E501

        :return: The git of this SourceSourceContext.  # noqa: E501
        :rtype: SourceGitSourceContext
        """
        return self._git

    @git.setter
    def git(self, git):
        """Sets the git of this SourceSourceContext.

        A SourceContext referring to any third party Git repo (e.g., GitHub).  # noqa: E501

        :param git: The git of this SourceSourceContext.  # noqa: E501
        :type: SourceGitSourceContext
        """

        self._git = git

    @property
    def labels(self):
        """Gets the labels of this SourceSourceContext.  # noqa: E501

        Labels with user defined metadata.  # noqa: E501

        :return: The labels of this SourceSourceContext.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this SourceSourceContext.

        Labels with user defined metadata.  # noqa: E501

        :param labels: The labels of this SourceSourceContext.  # noqa: E501
        :type: dict(str, str)
        """

        self._labels = labels

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
        if issubclass(SourceSourceContext, dict):
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
        if not isinstance(other, SourceSourceContext):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
