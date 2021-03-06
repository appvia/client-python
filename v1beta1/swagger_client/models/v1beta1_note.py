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
from swagger_client.models.attestation_authority import AttestationAuthority  # noqa: F401,E501
from swagger_client.models.build_build import BuildBuild  # noqa: F401,E501
from swagger_client.models.deployment_deployable import DeploymentDeployable  # noqa: F401,E501
from swagger_client.models.discovery_discovery import DiscoveryDiscovery  # noqa: F401,E501
from swagger_client.models.image_basis import ImageBasis  # noqa: F401,E501
from swagger_client.models.package_package import PackagePackage  # noqa: F401,E501
from swagger_client.models.v1beta1_note_kind import V1beta1NoteKind  # noqa: F401,E501
from swagger_client.models.v1beta1_related_url import V1beta1RelatedUrl  # noqa: F401,E501
from swagger_client.models.vulnerability_vulnerability import VulnerabilityVulnerability  # noqa: F401,E501


class V1beta1Note(object):
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
        'name': 'str',
        'short_description': 'str',
        'long_description': 'str',
        'kind': 'V1beta1NoteKind',
        'related_url': 'list[V1beta1RelatedUrl]',
        'expiration_time': 'datetime',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'related_note_names': 'list[str]',
        'vulnerability': 'VulnerabilityVulnerability',
        'build': 'BuildBuild',
        'base_image': 'ImageBasis',
        'package': 'PackagePackage',
        'deployable': 'DeploymentDeployable',
        'discovery': 'DiscoveryDiscovery',
        'attestation_authority': 'AttestationAuthority'
    }

    attribute_map = {
        'name': 'name',
        'short_description': 'short_description',
        'long_description': 'long_description',
        'kind': 'kind',
        'related_url': 'related_url',
        'expiration_time': 'expiration_time',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'related_note_names': 'related_note_names',
        'vulnerability': 'vulnerability',
        'build': 'build',
        'base_image': 'base_image',
        'package': 'package',
        'deployable': 'deployable',
        'discovery': 'discovery',
        'attestation_authority': 'attestation_authority'
    }

    def __init__(self, name=None, short_description=None, long_description=None, kind=None, related_url=None, expiration_time=None, create_time=None, update_time=None, related_note_names=None, vulnerability=None, build=None, base_image=None, package=None, deployable=None, discovery=None, attestation_authority=None):  # noqa: E501
        """V1beta1Note - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._short_description = None
        self._long_description = None
        self._kind = None
        self._related_url = None
        self._expiration_time = None
        self._create_time = None
        self._update_time = None
        self._related_note_names = None
        self._vulnerability = None
        self._build = None
        self._base_image = None
        self._package = None
        self._deployable = None
        self._discovery = None
        self._attestation_authority = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if short_description is not None:
            self.short_description = short_description
        if long_description is not None:
            self.long_description = long_description
        if kind is not None:
            self.kind = kind
        if related_url is not None:
            self.related_url = related_url
        if expiration_time is not None:
            self.expiration_time = expiration_time
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if related_note_names is not None:
            self.related_note_names = related_note_names
        if vulnerability is not None:
            self.vulnerability = vulnerability
        if build is not None:
            self.build = build
        if base_image is not None:
            self.base_image = base_image
        if package is not None:
            self.package = package
        if deployable is not None:
            self.deployable = deployable
        if discovery is not None:
            self.discovery = discovery
        if attestation_authority is not None:
            self.attestation_authority = attestation_authority

    @property
    def name(self):
        """Gets the name of this V1beta1Note.  # noqa: E501

        Output only. The name of the note in the form of `projects/[PROVIDER_ID]/notes/[NOTE_ID]`.  # noqa: E501

        :return: The name of this V1beta1Note.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1beta1Note.

        Output only. The name of the note in the form of `projects/[PROVIDER_ID]/notes/[NOTE_ID]`.  # noqa: E501

        :param name: The name of this V1beta1Note.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def short_description(self):
        """Gets the short_description of this V1beta1Note.  # noqa: E501

        A one sentence description of this note.  # noqa: E501

        :return: The short_description of this V1beta1Note.  # noqa: E501
        :rtype: str
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """Sets the short_description of this V1beta1Note.

        A one sentence description of this note.  # noqa: E501

        :param short_description: The short_description of this V1beta1Note.  # noqa: E501
        :type: str
        """

        self._short_description = short_description

    @property
    def long_description(self):
        """Gets the long_description of this V1beta1Note.  # noqa: E501

        A detailed description of this note.  # noqa: E501

        :return: The long_description of this V1beta1Note.  # noqa: E501
        :rtype: str
        """
        return self._long_description

    @long_description.setter
    def long_description(self, long_description):
        """Sets the long_description of this V1beta1Note.

        A detailed description of this note.  # noqa: E501

        :param long_description: The long_description of this V1beta1Note.  # noqa: E501
        :type: str
        """

        self._long_description = long_description

    @property
    def kind(self):
        """Gets the kind of this V1beta1Note.  # noqa: E501


        :return: The kind of this V1beta1Note.  # noqa: E501
        :rtype: V1beta1NoteKind
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this V1beta1Note.


        :param kind: The kind of this V1beta1Note.  # noqa: E501
        :type: V1beta1NoteKind
        """

        self._kind = kind

    @property
    def related_url(self):
        """Gets the related_url of this V1beta1Note.  # noqa: E501

        URLs associated with this note.  # noqa: E501

        :return: The related_url of this V1beta1Note.  # noqa: E501
        :rtype: list[V1beta1RelatedUrl]
        """
        return self._related_url

    @related_url.setter
    def related_url(self, related_url):
        """Sets the related_url of this V1beta1Note.

        URLs associated with this note.  # noqa: E501

        :param related_url: The related_url of this V1beta1Note.  # noqa: E501
        :type: list[V1beta1RelatedUrl]
        """

        self._related_url = related_url

    @property
    def expiration_time(self):
        """Gets the expiration_time of this V1beta1Note.  # noqa: E501

        Time of expiration for this note. Empty if note does not expire.  # noqa: E501

        :return: The expiration_time of this V1beta1Note.  # noqa: E501
        :rtype: datetime
        """
        return self._expiration_time

    @expiration_time.setter
    def expiration_time(self, expiration_time):
        """Sets the expiration_time of this V1beta1Note.

        Time of expiration for this note. Empty if note does not expire.  # noqa: E501

        :param expiration_time: The expiration_time of this V1beta1Note.  # noqa: E501
        :type: datetime
        """

        self._expiration_time = expiration_time

    @property
    def create_time(self):
        """Gets the create_time of this V1beta1Note.  # noqa: E501

        Output only. The time this note was created. This field can be used as a filter in list requests.  # noqa: E501

        :return: The create_time of this V1beta1Note.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this V1beta1Note.

        Output only. The time this note was created. This field can be used as a filter in list requests.  # noqa: E501

        :param create_time: The create_time of this V1beta1Note.  # noqa: E501
        :type: datetime
        """

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this V1beta1Note.  # noqa: E501

        Output only. The time this note was last updated. This field can be used as a filter in list requests.  # noqa: E501

        :return: The update_time of this V1beta1Note.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this V1beta1Note.

        Output only. The time this note was last updated. This field can be used as a filter in list requests.  # noqa: E501

        :param update_time: The update_time of this V1beta1Note.  # noqa: E501
        :type: datetime
        """

        self._update_time = update_time

    @property
    def related_note_names(self):
        """Gets the related_note_names of this V1beta1Note.  # noqa: E501

        Other notes related to this note.  # noqa: E501

        :return: The related_note_names of this V1beta1Note.  # noqa: E501
        :rtype: list[str]
        """
        return self._related_note_names

    @related_note_names.setter
    def related_note_names(self, related_note_names):
        """Sets the related_note_names of this V1beta1Note.

        Other notes related to this note.  # noqa: E501

        :param related_note_names: The related_note_names of this V1beta1Note.  # noqa: E501
        :type: list[str]
        """

        self._related_note_names = related_note_names

    @property
    def vulnerability(self):
        """Gets the vulnerability of this V1beta1Note.  # noqa: E501


        :return: The vulnerability of this V1beta1Note.  # noqa: E501
        :rtype: VulnerabilityVulnerability
        """
        return self._vulnerability

    @vulnerability.setter
    def vulnerability(self, vulnerability):
        """Sets the vulnerability of this V1beta1Note.


        :param vulnerability: The vulnerability of this V1beta1Note.  # noqa: E501
        :type: VulnerabilityVulnerability
        """

        self._vulnerability = vulnerability

    @property
    def build(self):
        """Gets the build of this V1beta1Note.  # noqa: E501


        :return: The build of this V1beta1Note.  # noqa: E501
        :rtype: BuildBuild
        """
        return self._build

    @build.setter
    def build(self, build):
        """Sets the build of this V1beta1Note.


        :param build: The build of this V1beta1Note.  # noqa: E501
        :type: BuildBuild
        """

        self._build = build

    @property
    def base_image(self):
        """Gets the base_image of this V1beta1Note.  # noqa: E501


        :return: The base_image of this V1beta1Note.  # noqa: E501
        :rtype: ImageBasis
        """
        return self._base_image

    @base_image.setter
    def base_image(self, base_image):
        """Sets the base_image of this V1beta1Note.


        :param base_image: The base_image of this V1beta1Note.  # noqa: E501
        :type: ImageBasis
        """

        self._base_image = base_image

    @property
    def package(self):
        """Gets the package of this V1beta1Note.  # noqa: E501


        :return: The package of this V1beta1Note.  # noqa: E501
        :rtype: PackagePackage
        """
        return self._package

    @package.setter
    def package(self, package):
        """Sets the package of this V1beta1Note.


        :param package: The package of this V1beta1Note.  # noqa: E501
        :type: PackagePackage
        """

        self._package = package

    @property
    def deployable(self):
        """Gets the deployable of this V1beta1Note.  # noqa: E501


        :return: The deployable of this V1beta1Note.  # noqa: E501
        :rtype: DeploymentDeployable
        """
        return self._deployable

    @deployable.setter
    def deployable(self, deployable):
        """Sets the deployable of this V1beta1Note.


        :param deployable: The deployable of this V1beta1Note.  # noqa: E501
        :type: DeploymentDeployable
        """

        self._deployable = deployable

    @property
    def discovery(self):
        """Gets the discovery of this V1beta1Note.  # noqa: E501


        :return: The discovery of this V1beta1Note.  # noqa: E501
        :rtype: DiscoveryDiscovery
        """
        return self._discovery

    @discovery.setter
    def discovery(self, discovery):
        """Sets the discovery of this V1beta1Note.


        :param discovery: The discovery of this V1beta1Note.  # noqa: E501
        :type: DiscoveryDiscovery
        """

        self._discovery = discovery

    @property
    def attestation_authority(self):
        """Gets the attestation_authority of this V1beta1Note.  # noqa: E501


        :return: The attestation_authority of this V1beta1Note.  # noqa: E501
        :rtype: AttestationAuthority
        """
        return self._attestation_authority

    @attestation_authority.setter
    def attestation_authority(self, attestation_authority):
        """Sets the attestation_authority of this V1beta1Note.


        :param attestation_authority: The attestation_authority of this V1beta1Note.  # noqa: E501
        :type: AttestationAuthority
        """

        self._attestation_authority = attestation_authority

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
        if issubclass(V1beta1Note, dict):
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
        if not isinstance(other, V1beta1Note):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
