import connexion
from stablemanager.models.action import Action
from stablemanager.models.action_summary import ActionSummary
from stablemanager.models.api_response import ApiResponse
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def add_action(body):
    """
    Adds a new action
    
    :param body: New action instance
    :type body: list | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = [Action.from_dict(d) for d in connexion.request.get_json()]
    return 'do some magic!'


def cancel_action(id, body):
    """
    Cancels an action
    
    :param id: 
    :type id: int
    :param body: comments
    :type body: str

    :rtype: None
    """
    return 'do some magic!'


def complete_action(id, body):
    """
    Completed an action
    
    :param id: 
    :type id: int
    :param body: comments
    :type body: str

    :rtype: None
    """
    return 'do some magic!'


def delete_action(id):
    """
    Deletes action data
    
    :param id: 
    :type id: int

    :rtype: None
    """
    return 'do some magic!'


def get_action(id):
    """
    Gets action data
    
    :param id: 
    :type id: int

    :rtype: Action
    """
    return 'do some magic!'


def get_actions(horse=None, date=None, status=None):
    """
    Gets list of actions
    
    :param horse: 
    :type horse: str
    :param date: 
    :type date: str
    :param status: 
    :type status: str

    :rtype: List[ActionSummary]
    """
    return 'do some magic!'


def update_action(body):
    """
    Updates an action
    
    :param body: Updated action instance
    :type body: list | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = [Action.from_dict(d) for d in connexion.request.get_json()]
    return 'do some magic!'
