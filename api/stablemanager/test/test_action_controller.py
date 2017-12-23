# coding: utf-8

from __future__ import absolute_import

from stablemanager.models.action import Action
from stablemanager.models.action_summary import ActionSummary
from stablemanager.models.api_response import ApiResponse
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestActionController(BaseTestCase):
    """ ActionController integration test stubs """

    def test_add_action(self):
        """
        Test case for add_action

        Adds a new action
        """
        body = [Action()]
        response = self.client.open('/v1/action',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_cancel_action(self):
        """
        Test case for cancel_action

        Cancels an action
        """
        body = 'body_example'
        response = self.client.open('/v1/action/{id}/cancel'.format(id=56),
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_complete_action(self):
        """
        Test case for complete_action

        Completed an action
        """
        body = 'body_example'
        response = self.client.open('/v1/action/{id}/complete'.format(id=56),
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_delete_action(self):
        """
        Test case for delete_action

        Deletes action data
        """
        response = self.client.open('/v1/action/{id}'.format(id=56),
                                    method='DELETE',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_action(self):
        """
        Test case for get_action

        Gets action data
        """
        response = self.client.open('/v1/action/{id}'.format(id=56),
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_actions(self):
        """
        Test case for get_actions

        Gets list of actions
        """
        query_string = [('horse', 'horse_example'),
                        ('date', 'date_example'),
                        ('status', 'status_example')]
        response = self.client.open('/v1/action',
                                    method='GET',
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_update_action(self):
        """
        Test case for update_action

        Updates an action
        """
        body = [Action()]
        response = self.client.open('/v1/action',
                                    method='PUT',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
