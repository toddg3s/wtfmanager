# coding: utf-8

from __future__ import absolute_import

from stablemanager.models.api_response import ApiResponse
from stablemanager.models.horse import Horse
from stablemanager.models.person import Person
from stablemanager.models.schedule_summary import ScheduleSummary
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestPersonController(BaseTestCase):
    """ PersonController integration test stubs """

    def test_add_person(self):
        """
        Test case for add_person

        Adds a new person
        """
        body = Person()
        response = self.client.open('/v1/person',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_delete_person(self):
        """
        Test case for delete_person

        Removes a person
        """
        response = self.client.open('/v1/person/{id}'.format(id='id_example'),
                                    method='DELETE',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_people(self):
        """
        Test case for get_people

        Retrieves a list of people
        """
        query_string = [('tags', 'tags_example')]
        response = self.client.open('/v1/person',
                                    method='GET',
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_person(self):
        """
        Test case for get_person

        Retrieves a person
        """
        response = self.client.open('/v1/person/{id}'.format(id='id_example'),
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_person_horses(self):
        """
        Test case for get_person_horses

        Retrieves a list of horses associated with a person
        """
        response = self.client.open('/v1/person/{id}/horses'.format(id='id_example'),
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_person_schedule(self):
        """
        Test case for get_person_schedule

        Retrieves a list of scheduled actions
        """
        response = self.client.open('/v1/person/{id}/schedule'.format(id='id_example'),
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_update_person(self):
        """
        Test case for update_person

        Updates a person
        """
        body = Person()
        response = self.client.open('/v1/person',
                                    method='PUT',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
