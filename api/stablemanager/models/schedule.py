# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Schedule(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id: str=None, summary: str=None, horse_id: str=None, person_id: str=None, period: str=None, count: int=None, days_of_week: List[str]=None, days_of_month: List[int]=None, time_of_day: str=None, start: date=None, end: date=None, num_occurrences: int=None, auto_complete: bool=None, tags: List[str]=None):
        """
        Schedule - a model defined in Swagger

        :param id: The id of this Schedule.
        :type id: str
        :param summary: The summary of this Schedule.
        :type summary: str
        :param horse_id: The horse_id of this Schedule.
        :type horse_id: str
        :param person_id: The person_id of this Schedule.
        :type person_id: str
        :param period: The period of this Schedule.
        :type period: str
        :param count: The count of this Schedule.
        :type count: int
        :param days_of_week: The days_of_week of this Schedule.
        :type days_of_week: List[str]
        :param days_of_month: The days_of_month of this Schedule.
        :type days_of_month: List[int]
        :param time_of_day: The time_of_day of this Schedule.
        :type time_of_day: str
        :param start: The start of this Schedule.
        :type start: date
        :param end: The end of this Schedule.
        :type end: date
        :param num_occurrences: The num_occurrences of this Schedule.
        :type num_occurrences: int
        :param auto_complete: The auto_complete of this Schedule.
        :type auto_complete: bool
        :param tags: The tags of this Schedule.
        :type tags: List[str]
        """
        self.swagger_types = {
            'id': str,
            'summary': str,
            'horse_id': str,
            'person_id': str,
            'period': str,
            'count': int,
            'days_of_week': List[str],
            'days_of_month': List[int],
            'time_of_day': str,
            'start': date,
            'end': date,
            'num_occurrences': int,
            'auto_complete': bool,
            'tags': List[str]
        }

        self.attribute_map = {
            'id': 'id',
            'summary': 'summary',
            'horse_id': 'horse_id',
            'person_id': 'person_id',
            'period': 'period',
            'count': 'count',
            'days_of_week': 'days_of_week',
            'days_of_month': 'days_of_month',
            'time_of_day': 'time_of_day',
            'start': 'start',
            'end': 'end',
            'num_occurrences': 'num_occurrences',
            'auto_complete': 'auto_complete',
            'tags': 'tags'
        }

        self._id = id
        self._summary = summary
        self._horse_id = horse_id
        self._person_id = person_id
        self._period = period
        self._count = count
        self._days_of_week = days_of_week
        self._days_of_month = days_of_month
        self._time_of_day = time_of_day
        self._start = start
        self._end = end
        self._num_occurrences = num_occurrences
        self._auto_complete = auto_complete
        self._tags = tags

    @classmethod
    def from_dict(cls, dikt) -> 'Schedule':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Schedule of this Schedule.
        :rtype: Schedule
        """
        return deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """
        Gets the id of this Schedule.

        :return: The id of this Schedule.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """
        Sets the id of this Schedule.

        :param id: The id of this Schedule.
        :type id: str
        """

        self._id = id

    @property
    def summary(self) -> str:
        """
        Gets the summary of this Schedule.

        :return: The summary of this Schedule.
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary: str):
        """
        Sets the summary of this Schedule.

        :param summary: The summary of this Schedule.
        :type summary: str
        """

        self._summary = summary

    @property
    def horse_id(self) -> str:
        """
        Gets the horse_id of this Schedule.

        :return: The horse_id of this Schedule.
        :rtype: str
        """
        return self._horse_id

    @horse_id.setter
    def horse_id(self, horse_id: str):
        """
        Sets the horse_id of this Schedule.

        :param horse_id: The horse_id of this Schedule.
        :type horse_id: str
        """

        self._horse_id = horse_id

    @property
    def person_id(self) -> str:
        """
        Gets the person_id of this Schedule.

        :return: The person_id of this Schedule.
        :rtype: str
        """
        return self._person_id

    @person_id.setter
    def person_id(self, person_id: str):
        """
        Sets the person_id of this Schedule.

        :param person_id: The person_id of this Schedule.
        :type person_id: str
        """

        self._person_id = person_id

    @property
    def period(self) -> str:
        """
        Gets the period of this Schedule.

        :return: The period of this Schedule.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period: str):
        """
        Sets the period of this Schedule.

        :param period: The period of this Schedule.
        :type period: str
        """
        allowed_values = ["daily", "weekly", "monthly", "annually", "one-time"]
        if period not in allowed_values:
            raise ValueError(
                "Invalid value for `period` ({0}), must be one of {1}"
                .format(period, allowed_values)
            )

        self._period = period

    @property
    def count(self) -> int:
        """
        Gets the count of this Schedule.

        :return: The count of this Schedule.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count: int):
        """
        Sets the count of this Schedule.

        :param count: The count of this Schedule.
        :type count: int
        """

        self._count = count

    @property
    def days_of_week(self) -> List[str]:
        """
        Gets the days_of_week of this Schedule.

        :return: The days_of_week of this Schedule.
        :rtype: List[str]
        """
        return self._days_of_week

    @days_of_week.setter
    def days_of_week(self, days_of_week: List[str]):
        """
        Sets the days_of_week of this Schedule.

        :param days_of_week: The days_of_week of this Schedule.
        :type days_of_week: List[str]
        """
        allowed_values = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
        if not set(days_of_week).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `days_of_week` [{0}], must be a subset of [{1}]"
                .format(", ".join(map(str, set(days_of_week)-set(allowed_values))),
                        ", ".join(map(str, allowed_values)))
            )

        self._days_of_week = days_of_week

    @property
    def days_of_month(self) -> List[int]:
        """
        Gets the days_of_month of this Schedule.

        :return: The days_of_month of this Schedule.
        :rtype: List[int]
        """
        return self._days_of_month

    @days_of_month.setter
    def days_of_month(self, days_of_month: List[int]):
        """
        Sets the days_of_month of this Schedule.

        :param days_of_month: The days_of_month of this Schedule.
        :type days_of_month: List[int]
        """

        self._days_of_month = days_of_month

    @property
    def time_of_day(self) -> str:
        """
        Gets the time_of_day of this Schedule.

        :return: The time_of_day of this Schedule.
        :rtype: str
        """
        return self._time_of_day

    @time_of_day.setter
    def time_of_day(self, time_of_day: str):
        """
        Sets the time_of_day of this Schedule.

        :param time_of_day: The time_of_day of this Schedule.
        :type time_of_day: str
        """

        self._time_of_day = time_of_day

    @property
    def start(self) -> date:
        """
        Gets the start of this Schedule.

        :return: The start of this Schedule.
        :rtype: date
        """
        return self._start

    @start.setter
    def start(self, start: date):
        """
        Sets the start of this Schedule.

        :param start: The start of this Schedule.
        :type start: date
        """

        self._start = start

    @property
    def end(self) -> date:
        """
        Gets the end of this Schedule.

        :return: The end of this Schedule.
        :rtype: date
        """
        return self._end

    @end.setter
    def end(self, end: date):
        """
        Sets the end of this Schedule.

        :param end: The end of this Schedule.
        :type end: date
        """

        self._end = end

    @property
    def num_occurrences(self) -> int:
        """
        Gets the num_occurrences of this Schedule.

        :return: The num_occurrences of this Schedule.
        :rtype: int
        """
        return self._num_occurrences

    @num_occurrences.setter
    def num_occurrences(self, num_occurrences: int):
        """
        Sets the num_occurrences of this Schedule.

        :param num_occurrences: The num_occurrences of this Schedule.
        :type num_occurrences: int
        """

        self._num_occurrences = num_occurrences

    @property
    def auto_complete(self) -> bool:
        """
        Gets the auto_complete of this Schedule.

        :return: The auto_complete of this Schedule.
        :rtype: bool
        """
        return self._auto_complete

    @auto_complete.setter
    def auto_complete(self, auto_complete: bool):
        """
        Sets the auto_complete of this Schedule.

        :param auto_complete: The auto_complete of this Schedule.
        :type auto_complete: bool
        """

        self._auto_complete = auto_complete

    @property
    def tags(self) -> List[str]:
        """
        Gets the tags of this Schedule.

        :return: The tags of this Schedule.
        :rtype: List[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags: List[str]):
        """
        Sets the tags of this Schedule.

        :param tags: The tags of this Schedule.
        :type tags: List[str]
        """

        self._tags = tags

