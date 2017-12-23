# coding: utf-8

from __future__ import absolute_import

from stablemanager.models.api_response import ApiResponse
from stablemanager.models.schedule import Schedule
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestScheduleController(BaseTestCase):
    """ ScheduleController integration test stubs """

    def test_add_schedule(self):
        """
        Test case for add_schedule

        Adds a new schedule
        """
        body = Schedule()
        response = self.client.open('/v1/schedule',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_delete_schedule(self):
        """
        Test case for delete_schedule

        Deletes a schedule
        """
        response = self.client.open('/v1/schedule/{id}'.format(id=56),
                                    method='DELETE',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_schedule(self):
        """
        Test case for get_schedule

        Retrieves a schedule
        """
        response = self.client.open('/v1/schedule/{id}'.format(id=56),
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_update_schedule(self):
        """
        Test case for update_schedule

        Updates a schedule
        """
        body = Schedule()
        response = self.client.open('/v1/schedule',
                                    method='PUT',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
