from typing import GenericMeta
from datetime import datetime, date
from six import integer_types, iteritems


def _deserialize(data, klass):
    """
    Deserializes dict, list, str into an object.

    :param data: dict, list or str.
    :param klass: class literal, or string of class name.

    :return: object.
    """
    if data is None:
        return None

    if klass in integer_types or klass in (float, str, bool):
        return _deserialize_primitive(data, klass)
    elif klass == object:
        return _deserialize_object(data)
    elif klass == date:
        return deserialize_date(data)
    elif klass == datetime:
        return deserialize_datetime(data)
    elif type(klass) == GenericMeta:
        if klass.__extra__ == list:
            return _deserialize_list(data, klass.__args__[0])
        if klass.__extra__ == dict:
            return _deserialize_dict(data, klass.__args__[1])
    else:
        return deserialize_model(data, klass)


def _deserialize_primitive(data, klass):
    """
    Deserializes to primitive type.

    :param data: data to deserialize.
    :param klass: class literal.

    :return: int, long, float, str, bool.
    :rtype: int | long | float | str | bool
    """
    try:
        value = klass(data)
    except UnicodeEncodeError:
        value = unicode(data)
    except TypeError:
        value = data
    return value


def _deserialize_object(value):
    """
    Return a original value.

    :return: object.
    """
    return value


def deserialize_date(string):
    """
    Deserializes string to date.

    :param string: str.
    :type string: str
    :return: date.
    :rtype: date
    """
    try:
        from dateutil.parser import parse
        return parse(string).date()
    except ImportError:
        return string


def deserialize_datetime(string):
    """
    Deserializes string to datetime.

    The string should be in iso8601 datetime format.

    :param string: str.
    :type string: str
    :return: datetime.
    :rtype: datetime
    """
    try:
        from dateutil.parser import parse
        return parse(string)
    except ImportError:
        return string


def deserialize_model(data, klass):
    """
    Deserializes list or dict to model.

    :param data: dict, list.
    :type data: dict | list
    :param klass: class literal.
    :return: model object.
    """
    instance = klass()

    if not instance.swagger_types:
        return data

    for attr, attr_type in iteritems(instance.swagger_types):
        if data is not None \
                and instance.attribute_map[attr] in data \
                and isinstance(data, (list, dict)):
            value = data[instance.attribute_map[attr]]
            setattr(instance, attr, _deserialize(value, attr_type))

    return instance


def _deserialize_list(data, boxed_type):
    """
    Deserializes a list and its elements.

    :param data: list to deserialize.
    :type data: list
    :param boxed_type: class literal.

    :return: deserialized list.
    :rtype: list
    """
    return [_deserialize(sub_data, boxed_type)
            for sub_data in data]



def _deserialize_dict(data, boxed_type):
    """
    Deserializes a dict and its elements.

    :param data: dict to deserialize.
    :type data: dict
    :param boxed_type: class literal.

    :return: deserialized dict.
    :rtype: dict
    """
    return {k: _deserialize(v, boxed_type)
            for k, v in iteritems(data)}


def get_schedule_summary_text(schedule):
    """
    Returns a descriptive text for the schedule
    :param schedule:
    :type schedule: stablemanager.models.Schedule
    :return:
    """
    if schedule.period == 'one-time':
        return 'Once on %s %s' % (schedule.start, get_time_of_day_text(schedule.time_of_day))

    text = "Every "
    plural = ""
    if schedule.count > 1:
        text += str(schedule.count)
        plural = "s"
    if schedule.period == 'daily':
        text += 'day' + plural
    elif schedule.period == 'weekly':
        text += 'week' + plural
        text += ' on ' + ','.join(schedule.days_of_week)
    elif schedule.period == 'monthly':
        text += 'month' + plural
        if schedule.days_of_month is None or schedule.days_of_month.count() == 0:
            text += ' on the 1st'
        else:
            days = []
            for day in schedule.days_of_month:
                ord = day % 10
                if ord == 1:
                    ordtext = 'st'
                elif ord == 2:
                    ordtext = 'nd'
                elif ord == 3:
                    ordtext = 'rd'
                else:
                    ordtext = 'th'
                days.append('%d%s' % (day, ordtext))
            text += ' on the ' + ','.join(days)
    elif schedule.period == 'anually':
        text += 'year' + plural
        text += ' on ' + schedule.start.strftime('%b %d')

    text += ' ' + get_time_of_day_text(schedule.time_of_day)
    text += ' starting on ' + schedule.start.strftime('%b %d, %Y')
    if schedule.num_occurrences is not None and schedule.num_occurrences > 0:
        text += ' %d times'
    elif schedule.end is not None:
        text += schedule.end.strftime(' until %b %d, %Y')
    return text


def get_time_of_day_text(time_of_day):
    if time_of_day is None or len(time_of_day) == 0:
        return ''
    if time_of_day == 'morning' or time_of_day == 'afternoon' or time_of_day == 'evening':
        return 'in the ' + time_of_day
    elif time_of_day == 'night':
        return 'at night'
    else:
        return 'at ' + time_of_day
