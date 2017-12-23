import connexion
from stablemanager.models.api_response import ApiResponse
from stablemanager.models.schedule import Schedule
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def add_schedule(body):
    """
    Adds a new schedule
    
    :param body: Schedule object to add
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Schedule.from_dict(connexion.request.get_json())
    return 'do some magic!'


def delete_schedule(id):
    """
    Deletes a schedule
    
    :param id: Identifier of the schedule
    :type id: int

    :rtype: None
    """
    return 'do some magic!'


def get_schedule(id):
    """
    Retrieves a schedule
    
    :param id: Identifier of the schedule
    :type id: int

    :rtype: Schedule
    """
    return 'do some magic!'


def update_schedule(body):
    """
    Updates a schedule
    
    :param body: Schedule object to update
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Schedule.from_dict(connexion.request.get_json())
    return 'do some magic!'
