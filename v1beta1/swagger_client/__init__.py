# coding: utf-8

# flake8: noqa

"""
    grafeas.proto

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: version not set
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from swagger_client.api.grafeas_v1_beta1_api import GrafeasV1Beta1Api
# import ApiClient
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
# import models into sdk package
from swagger_client.models.alias_context_kind import AliasContextKind
from swagger_client.models.attestation_attestation import AttestationAttestation
from swagger_client.models.attestation_authority import AttestationAuthority
from swagger_client.models.attestation_generic_signed_attestation import AttestationGenericSignedAttestation
from swagger_client.models.attestation_generic_signed_attestation_content_type import AttestationGenericSignedAttestationContentType
from swagger_client.models.attestation_pgp_signed_attestation import AttestationPgpSignedAttestation
from swagger_client.models.attestation_pgp_signed_attestation_content_type import AttestationPgpSignedAttestationContentType
from swagger_client.models.authority_hint import AuthorityHint
from swagger_client.models.build_build import BuildBuild
from swagger_client.models.build_build_signature import BuildBuildSignature
from swagger_client.models.build_signature_key_type import BuildSignatureKeyType
from swagger_client.models.cvs_sv3_attack_complexity import CVSSv3AttackComplexity
from swagger_client.models.cvs_sv3_attack_vector import CVSSv3AttackVector
from swagger_client.models.cvs_sv3_impact import CVSSv3Impact
from swagger_client.models.cvs_sv3_privileges_required import CVSSv3PrivilegesRequired
from swagger_client.models.cvs_sv3_scope import CVSSv3Scope
from swagger_client.models.cvs_sv3_user_interaction import CVSSv3UserInteraction
from swagger_client.models.deployment_deployable import DeploymentDeployable
from swagger_client.models.deployment_deployment import DeploymentDeployment
from swagger_client.models.deployment_platform import DeploymentPlatform
from swagger_client.models.discovered_analysis_status import DiscoveredAnalysisStatus
from swagger_client.models.discovered_continuous_analysis import DiscoveredContinuousAnalysis
from swagger_client.models.discovery_discovered import DiscoveryDiscovered
from swagger_client.models.discovery_discovery import DiscoveryDiscovery
from swagger_client.models.hash_hash_type import HashHashType
from swagger_client.models.image_basis import ImageBasis
from swagger_client.models.image_derived import ImageDerived
from swagger_client.models.image_fingerprint import ImageFingerprint
from swagger_client.models.image_layer import ImageLayer
from swagger_client.models.layer_directive import LayerDirective
from swagger_client.models.package_architecture import PackageArchitecture
from swagger_client.models.package_distribution import PackageDistribution
from swagger_client.models.package_installation import PackageInstallation
from swagger_client.models.package_package import PackagePackage
from swagger_client.models.package_version import PackageVersion
from swagger_client.models.protobuf_any import ProtobufAny
from swagger_client.models.protobuf_field_mask import ProtobufFieldMask
from swagger_client.models.provenance_artifact import ProvenanceArtifact
from swagger_client.models.provenance_build_provenance import ProvenanceBuildProvenance
from swagger_client.models.provenance_command import ProvenanceCommand
from swagger_client.models.provenance_file_hashes import ProvenanceFileHashes
from swagger_client.models.provenance_hash import ProvenanceHash
from swagger_client.models.provenance_source import ProvenanceSource
from swagger_client.models.rpc_status import RpcStatus
from swagger_client.models.source_alias_context import SourceAliasContext
from swagger_client.models.source_cloud_repo_source_context import SourceCloudRepoSourceContext
from swagger_client.models.source_gerrit_source_context import SourceGerritSourceContext
from swagger_client.models.source_git_source_context import SourceGitSourceContext
from swagger_client.models.source_project_repo_id import SourceProjectRepoId
from swagger_client.models.source_repo_id import SourceRepoId
from swagger_client.models.source_source_context import SourceSourceContext
from swagger_client.models.v1beta1_batch_create_notes_request import V1beta1BatchCreateNotesRequest
from swagger_client.models.v1beta1_batch_create_notes_response import V1beta1BatchCreateNotesResponse
from swagger_client.models.v1beta1_batch_create_occurrences_request import V1beta1BatchCreateOccurrencesRequest
from swagger_client.models.v1beta1_batch_create_occurrences_response import V1beta1BatchCreateOccurrencesResponse
from swagger_client.models.v1beta1_list_note_occurrences_response import V1beta1ListNoteOccurrencesResponse
from swagger_client.models.v1beta1_list_notes_response import V1beta1ListNotesResponse
from swagger_client.models.v1beta1_list_occurrences_response import V1beta1ListOccurrencesResponse
from swagger_client.models.v1beta1_note import V1beta1Note
from swagger_client.models.v1beta1_note_kind import V1beta1NoteKind
from swagger_client.models.v1beta1_occurrence import V1beta1Occurrence
from swagger_client.models.v1beta1_related_url import V1beta1RelatedUrl
from swagger_client.models.v1beta1_resource import V1beta1Resource
from swagger_client.models.v1beta1_signature import V1beta1Signature
from swagger_client.models.v1beta1_vulnerability_occurrences_summary import V1beta1VulnerabilityOccurrencesSummary
from swagger_client.models.v1beta1attestation_details import V1beta1attestationDetails
from swagger_client.models.v1beta1build_details import V1beta1buildDetails
from swagger_client.models.v1beta1deployment_details import V1beta1deploymentDetails
from swagger_client.models.v1beta1discovery_details import V1beta1discoveryDetails
from swagger_client.models.v1beta1image_details import V1beta1imageDetails
from swagger_client.models.v1beta1package_details import V1beta1packageDetails
from swagger_client.models.v1beta1package_location import V1beta1packageLocation
from swagger_client.models.v1beta1vulnerability_details import V1beta1vulnerabilityDetails
from swagger_client.models.version_version_kind import VersionVersionKind
from swagger_client.models.vulnerability_cvs_sv3 import VulnerabilityCVSSv3
from swagger_client.models.vulnerability_detail import VulnerabilityDetail
from swagger_client.models.vulnerability_occurrences_summary_fixable_total_by_digest import VulnerabilityOccurrencesSummaryFixableTotalByDigest
from swagger_client.models.vulnerability_package_issue import VulnerabilityPackageIssue
from swagger_client.models.vulnerability_severity import VulnerabilitySeverity
from swagger_client.models.vulnerability_vulnerability import VulnerabilityVulnerability
from swagger_client.models.vulnerability_vulnerability_location import VulnerabilityVulnerabilityLocation
from swagger_client.models.vulnerability_windows_detail import VulnerabilityWindowsDetail
from swagger_client.models.windows_detail_knowledge_base import WindowsDetailKnowledgeBase
