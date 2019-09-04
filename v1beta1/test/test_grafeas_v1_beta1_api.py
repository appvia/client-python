# coding: utf-8

"""
    grafeas.proto

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: version not set
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.grafeas_v1_beta1_api import GrafeasV1Beta1Api  # noqa: E501
from swagger_client.rest import ApiException


class TestGrafeasV1Beta1Api(unittest.TestCase):
    """GrafeasV1Beta1Api unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.grafeas_v1_beta1_api.GrafeasV1Beta1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_batch_create_notes(self):
        """Test case for batch_create_notes

        Creates new notes in batch.  # noqa: E501
        """
        pass

    def test_batch_create_occurrences(self):
        """Test case for batch_create_occurrences

        Creates new occurrences in batch.  # noqa: E501
        """
        pass

    def test_create_note(self):
        """Test case for create_note

        Creates a new note.  # noqa: E501
        """
        pass

    def test_create_occurrence(self):
        """Test case for create_occurrence

        Creates a new occurrence.  # noqa: E501
        """
        pass

    def test_delete_note(self):
        """Test case for delete_note

        Deletes the specified note.  # noqa: E501
        """
        pass

    def test_delete_occurrence(self):
        """Test case for delete_occurrence

        Deletes the specified occurrence. For example, use this method to delete an occurrence when the occurrence is no longer applicable for the given resource.  # noqa: E501
        """
        pass

    def test_get_note(self):
        """Test case for get_note

        Gets the specified note.  # noqa: E501
        """
        pass

    def test_get_occurrence(self):
        """Test case for get_occurrence

        Gets the specified occurrence.  # noqa: E501
        """
        pass

    def test_get_occurrence_note(self):
        """Test case for get_occurrence_note

        Gets the note attached to the specified occurrence. Consumer projects can use this method to get a note that belongs to a provider project.  # noqa: E501
        """
        pass

    def test_get_vulnerability_occurrences_summary(self):
        """Test case for get_vulnerability_occurrences_summary

        Gets a summary of the number and severity of occurrences.  # noqa: E501
        """
        pass

    def test_list_note_occurrences(self):
        """Test case for list_note_occurrences

        Lists occurrences referencing the specified note. Provider projects can use this method to get all occurrences across consumer projects referencing the specified note.  # noqa: E501
        """
        pass

    def test_list_notes(self):
        """Test case for list_notes

        Lists notes for the specified project.  # noqa: E501
        """
        pass

    def test_list_occurrences(self):
        """Test case for list_occurrences

        Lists occurrences for the specified project.  # noqa: E501
        """
        pass

    def test_update_note(self):
        """Test case for update_note

        Updates the specified note.  # noqa: E501
        """
        pass

    def test_update_occurrence(self):
        """Test case for update_occurrence

        Updates the specified occurrence.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
