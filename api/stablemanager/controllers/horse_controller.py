import connexion
from stablemanager.models.api_response import ApiResponse
from stablemanager.models.association import Association
from stablemanager.models.horse import Horse
from stablemanager.models.schedule_summary import ScheduleSummary
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime, get_schedule_summary_text
import uuid

from stablemanager.controllers import Data

def add_horse(body):
    """
    Adds a new horse to the barn
    
    :param body: Horse object to add to barn
    :type body: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        body = Horse.from_dict(connexion.request.get_json())
    horse = Data.get('horse', body.id)
    if horse is not None:
        return ApiResponse(code=422, type='warning', message='Horse with that id already exists'), 422

    Data.put(body)
    return 'Added', 202


def add_horse_people(id, body):
    """
    Adds a people to the horse
    
    :param id: Identifier of the horse
    :type id: str
    :param body: New association(s) to the horse
    :type body: list | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = [Association.from_dict(d) for d in connexion.request.get_json()]

    for a in body:
        if a.id is None or len(a.id) == 0:
            a.id = str(uuid.uuid4()).replace('-', '')
        a.horse_id = id
        Data.put(a)


def delete_horse(id):
    """
    Removes a horse from the barn
    
    :param id: Identifier of the horse
    :type id: str

    :rtype: None
    """

    for s in Data.get_horse_schedules(id):
        Data.delete(s)
    for a in Data.get_horse_people(id):
        Data.delete(a)
    Data.delete(Horse(id=id))


def delete_horse_person(id, assocId):
    """
    Removes association
    
    :param id: Identifier of the horse
    :type id: str
    :param assocId: Identifier of the association
    :type assocId: int

    :rtype: None
    """
    Data.delete(Association(id=assocId))


def get_horse(id):
    """
    Gets information for a specific horse
    
    :param id: Identifier of the horse
    :type id: str

    :rtype: Horse
    """
    horse = Data.get('horse', id)
    if horse is None:
        return 'Horse Not Found', 404
    else:
        return Horse.from_dict(horse)


def get_horse_people(id, type=None):
    """
    Retrieves a list of all people associated with the horse
    
    :param id: Identifier of the horse
    :type id: str
    :param type: restricts the list to specific types of people
    :type type: str

    :rtype: List[Association]
    """
    horse = Data.get('horse', id)
    if horse is None:
        return 'Horse Not Found', 404
    else:
        return Data.get_horse_people(id, type)


def get_horse_schedule(id):
    """
    Retrieves a list of scheduled actions
    
    :param id: Identifier of the horse
    :type id: str

    :rtype: List[ScheduleSummary]
    """
    return [ScheduleSummary(s.id, get_schedule_summary_text(s)) for s in Data.get_horse_schedules(id)]


def get_horses():
    """
    Retrieves a list of horses in the barn
    

    :rtype: List[Horse]
    """
    result = Data.query('horse').sort('name').go()
    horses = []
    for item in result:
        horses.append(Horse.from_dict(item))
    return horses


def update_horse(body):
    """
    Updates a horse&#39;s data
    
    :param body: Horse to add to barn
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Horse.from_dict(connexion.request.get_json())

    Data.put(body)


def update_horse_people(id, body):
    """
    Updates association(s)
    
    :param id: Identifier of the horse
    :type id: str
    :param body: Updated association(s) to the horse
    :type body: list | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = [Association.from_dict(d) for d in connexion.request.get_json()]
    return 'do some magic!'
