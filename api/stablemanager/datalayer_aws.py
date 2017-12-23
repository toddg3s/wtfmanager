from stablemanager.datalayer import DataProvider, QuerySpec
from stablemanager.models import *
import boto3
from boto3.dynamodb.conditions import Key, Attr


class AWSData(DataProvider):
    def get(self, datatype, dataid):
        db = boto3.resource('dynamodb')
        table = db.Table(datatype)
        result = table.get_item(Key={'id': dataid})
        if 'Item' in result:
            return result['Item']
        else:
            return None

    def put(self, dataobject):
        db = boto3.resource('dynamodb')
        table = db.Table(dataobject.__class__.__name__.lower())
        table.put_item(Item=dataobject.to_dict())

    def delete(self, dataobject):
        db = boto3.resource('dynamodb')
        table = db.Table(dataobject.__class__.__name__.lower())
        table.delete_item(Key={'id': dataobject.id})

    def query(self, datatype):
        return QuerySpec(datatype, self.doquery)
        pass

    def doquery(self, queryspec):
        db = boto3.resource('dynamodb')
        table = db.Table(queryspec.DataType)
        data = None
        if len(queryspec.Filters) == 0:
            response = table.scan()
            data = response['Items']
            while 'LastEvaluatedKey' in response:
                response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
                data.extend(response['Items'])
        else:
            for prop in queryspec.Filters:
                if data is None and queryspec.Filters[prop][2]:  # queryable
                    key = Key(prop)
                    if queryspec.Filters[prop][0] == '=':
                        expr = key.eq(queryspec.Filters[prop][1])
                    elif queryspec.Filters[prop][0] == '<':
                        expr = key.lt(queryspec.Filters[prop][1])
                    elif queryspec.Filters[prop][0] == '>':
                        expr = key.gt(queryspec.Filters[prop][1])
                    elif queryspec.Filters[prop][0] == '<=':
                        expr = key.lte(queryspec.Filters[prop][1])
                    elif queryspec.Filters[prop][0] == '>=':
                        expr = key.gte(queryspec.Filters[prop][1])
                    elif queryspec.Filters[prop][0] == 'btw':
                        expr = key.between(queryspec.Filters[prop][1][0], queryspec.Filters[prop][1][0])
                    response = table.query(KeyConditionExpression=expr)
                    data = response['Items']
                else:  # queryable = False
                    if data is None:
                        attr = Attr(prop)
                        if queryspec.Filters[prop][0] == '=':
                            expr = attr.eq(queryspec.Filters[prop][1])
                        elif queryspec.Filters[prop][0] == '<':
                            expr = attr.lt(queryspec.Filters[prop][1])
                        elif queryspec.Filters[prop][0] == '>':
                            expr = attr.gt(queryspec.Filters[prop][1])
                        elif queryspec.Filters[prop][0] == '<=':
                            expr = attr.lte(queryspec.Filters[prop][1])
                        elif queryspec.Filters[prop][0] == '>=':
                            expr = attr.gte(queryspec.Filters[prop][1])
                        elif queryspec.Filters[prop][0] == 'btw':
                            expr = attr.between(queryspec.Filters[prop][1][0], queryspec.Filters[prop][1][0])
                        response = table.scan(FilterExpression=expr)
                        data = response['Items']
                        while 'LastEvaluatedKey' in response:
                            response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
                            data.extend(response['Items'])
                    else:
                        pass  # TODO: Secondary value

        if data is None or len(data) == 0 or len(queryspec.Sorts) == 0:
            return data

        sortproperty = next(iter(queryspec.Sorts))
        sorteddata = sorted(data, key=lambda item: item[sortproperty])
        return sorteddata

    def get_actions(self, from_date, to_date):
        pass

    def get_horse_schedules(self, horse_id):
        db = boto3.resource('dynamodb')
        table = db.Table('schedule')
        response = table.query(IndexName="horse_id-index", KeyConditionExpression=Key('horse_id').eq(horse_id))
        if 'Items' not in response:
            return None
        else:
            return [Schedule.from_dict(s) for s in response['Items']]

    def get_horse_people(self, horse_id, person_type=None):
        horse = self.get('horse', horse_id)
        db = boto3.resource('dynamodb')
        table = db.Table('association')
        expr = None
        if person_type is not None:
            if type(person_type) is str:
                expr = Attr('type').is_in(str.split(person_type, ','))
            else:
                expr = Attr('type').is_in(person_type)
        if expr is None:
            response = table.query(IndexName="horse_id-index",
                                   KeyConditionExpression=Key('horse_id').eq(horse_id))
        else:
            response = table.query(IndexName="horse_id-index",
                                   KeyConditionExpression=Key('horse_id').eq(horse_id),
                                   FilterExpression=expr)

        if 'Items' not in response:
            return None
        else:
            people = []
            for a in response['Items']:
                person = self.get('person', a['person_id'])
                people.append(Association(a['id'], horse_id, horse['name'], a['person_id'],
                                          person['name'], a['type'], a['comments']))
            return people
