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

from swagger_client.models.attestation_generic_signed_attestation_content_type import AttestationGenericSignedAttestationContentType  # noqa: F401,E501
from swagger_client.models.v1beta1_signature import V1beta1Signature  # noqa: F401,E501


class AttestationGenericSignedAttestation(object):
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
        'content_type': 'AttestationGenericSignedAttestationContentType',
        'serialized_payload': 'str',
        'signatures': 'list[V1beta1Signature]'
    }

    attribute_map = {
        'content_type': 'content_type',
        'serialized_payload': 'serialized_payload',
        'signatures': 'signatures'
    }

    def __init__(self, content_type=None, serialized_payload=None, signatures=None):  # noqa: E501
        """AttestationGenericSignedAttestation - a model defined in Swagger"""  # noqa: E501

        self._content_type = None
        self._serialized_payload = None
        self._signatures = None
        self.discriminator = None

        if content_type is not None:
            self.content_type = content_type
        if serialized_payload is not None:
            self.serialized_payload = serialized_payload
        if signatures is not None:
            self.signatures = signatures

    @property
    def content_type(self):
        """Gets the content_type of this AttestationGenericSignedAttestation.  # noqa: E501

        Type (for example schema) of the attestation payload that was signed. The verifier must ensure that the provided type is one that the verifier supports, and that the attestation payload is a valid instantiation of that type (for example by validating a JSON schema).  # noqa: E501

        :return: The content_type of this AttestationGenericSignedAttestation.  # noqa: E501
        :rtype: AttestationGenericSignedAttestationContentType
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this AttestationGenericSignedAttestation.

        Type (for example schema) of the attestation payload that was signed. The verifier must ensure that the provided type is one that the verifier supports, and that the attestation payload is a valid instantiation of that type (for example by validating a JSON schema).  # noqa: E501

        :param content_type: The content_type of this AttestationGenericSignedAttestation.  # noqa: E501
        :type: AttestationGenericSignedAttestationContentType
        """

        self._content_type = content_type

    @property
    def serialized_payload(self):
        """Gets the serialized_payload of this AttestationGenericSignedAttestation.  # noqa: E501

        The serialized payload that is verified by one or more `signatures`. The encoding and semantic meaning of this payload must match what is set in `content_type`.  # noqa: E501

        :return: The serialized_payload of this AttestationGenericSignedAttestation.  # noqa: E501
        :rtype: str
        """
        return self._serialized_payload

    @serialized_payload.setter
    def serialized_payload(self, serialized_payload):
        """Sets the serialized_payload of this AttestationGenericSignedAttestation.

        The serialized payload that is verified by one or more `signatures`. The encoding and semantic meaning of this payload must match what is set in `content_type`.  # noqa: E501

        :param serialized_payload: The serialized_payload of this AttestationGenericSignedAttestation.  # noqa: E501
        :type: str
        """
        if serialized_payload is not None and not re.search(r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', serialized_payload):  # noqa: E501
            raise ValueError(r"Invalid value for `serialized_payload`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._serialized_payload = serialized_payload

    @property
    def signatures(self):
        """Gets the signatures of this AttestationGenericSignedAttestation.  # noqa: E501

        One or more signatures over `serialized_payload`.  Verifier implementations should consider this attestation message verified if at least one `signature` verifies `serialized_payload`.  See `Signature` in common.proto for more details on signature structure and verification.  # noqa: E501

        :return: The signatures of this AttestationGenericSignedAttestation.  # noqa: E501
        :rtype: list[V1beta1Signature]
        """
        return self._signatures

    @signatures.setter
    def signatures(self, signatures):
        """Sets the signatures of this AttestationGenericSignedAttestation.

        One or more signatures over `serialized_payload`.  Verifier implementations should consider this attestation message verified if at least one `signature` verifies `serialized_payload`.  See `Signature` in common.proto for more details on signature structure and verification.  # noqa: E501

        :param signatures: The signatures of this AttestationGenericSignedAttestation.  # noqa: E501
        :type: list[V1beta1Signature]
        """

        self._signatures = signatures

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
        if issubclass(AttestationGenericSignedAttestation, dict):
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
        if not isinstance(other, AttestationGenericSignedAttestation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
