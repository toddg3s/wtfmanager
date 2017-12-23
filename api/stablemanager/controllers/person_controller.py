import connexion
from stablemanager.models.api_response import ApiResponse
from stablemanager.models.horse import Horse
from stablemanager.models.person import Person
from stablemanager.models.schedule_summary import ScheduleSummary
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

from stablemanager.controllers import Data

def add_person(body=None):
    """
    Adds a new person
    
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Person.from_dict(connexion.request.get_json())
    Data.put(body)
    return 'Added', 202


def delete_person(id):
    """
    Removes a person
    
    :param id: RestrictsIdentifier of the person
    :type id: str

    :rtype: Person
    """
    return 'do some magic!'


def get_people(tags=None):
    """
    Retrieves a list of people
    
    :param tags: Restricts list to people having certain tags (comma-saprated list)
    :type tags: str

    :rtype: List[Person]
    """
    people = Data.query('person').go()
    return people


def get_person(id):
    """
    Retrieves a person
    
    :param id: RestrictsIdentifier of the person
    :type id: str

    :rtype: Person
    """
    person = Data.get('person', id)
    if person is None:
        return 'person not found', 404
    else:
        return person


def get_person_horses(id):
    """
    Retrieves a list of horses associated with a person
    
    :param id: RestrictsIdentifier of the person
    :type id: str

    :rtype: List[Horse]
    """
    return 'do some magic!'


def get_person_schedule(id):
    """
    Retrieves a list of scheduled actions
    
    :param id: Identifier of the person
    :type id: str

    :rtype: List[ScheduleSummary]
    """
    return 'do some magic!'


def update_person(body=None):
    """
    Updates a person
    
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Person.from_dict(connexion.request.get_json())

    Data.put(body)
    return 'Ok', 200
