# coding: utf-8

from __future__ import absolute_import

from stablemanager.models.api_response import ApiResponse
from stablemanager.models.association import Association
from stablemanager.models.horse import Horse
from stablemanager.models.schedule_summary import ScheduleSummary
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestHorseController(BaseTestCase):
    """ HorseController integration test stubs """

    def test_add_horse(self):
        """
        Test case for add_horse

        Adds a new horse to the barn
        """
        body = Horse()
        response = self.client.open('/v1/horse',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_add_horse_people(self):
        """
        Test case for add_horse_people

        Adds a people to the horse
        """
        body = [Association()]
        response = self.client.open('/v1/horse/{id}/people'.format(id='id_example'),
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_delete_horse(self):
        """
        Test case for delete_horse

        Removes a horse from the barn
        """
        response = self.client.open('/v1/horse/{id}'.format(id='id_example'),
                                    method='DELETE',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_delete_horse_person(self):
        """
        Test case for delete_horse_person

        Removes association
        """
        response = self.client.open('/v1/horse/{id}/people/{personId}'.format(id='id_example', personId='personId_example'),
                                    method='DELETE',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_horse(self):
        """
        Test case for get_horse

        Gets information for a specific horse
        """
        response = self.client.open('/v1/horse/{id}'.format(id='id_example'),
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_horse_people(self):
        """
        Test case for get_horse_people

        Retrieves a list of all people associated with the horse
        """
        query_string = [('type', 'type_example')]
        response = self.client.open('/v1/horse/{id}/people'.format(id='id_example'),
                                    method='GET',
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_horse_schedule(self):
        """
        Test case for get_horse_schedule

        Retrieves a list of scheduled actions
        """
        response = self.client.open('/v1/horse/{id}/schedule'.format(id='id_example'),
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_horses(self):
        """
        Test case for get_horses

        Retrieves a list of horses in the barn
        """
        response = self.client.open('/v1/horse',
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_update_horse(self):
        """
        Test case for update_horse

        Updates a horse's data
        """
        body = Horse()
        response = self.client.open('/v1/horse',
                                    method='PUT',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_update_horse_people(self):
        """
        Test case for update_horse_people

        Updates association(s)
        """
        body = [Association()]
        response = self.client.open('/v1/horse/{id}/people'.format(id='id_example'),
                                    method='PUT',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
