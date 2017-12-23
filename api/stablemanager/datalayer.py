
class DataProvider:
    def get(self, datatype, dataid):
        pass

    def put(self, dataobject):
        pass

    def delete(self, dataobject):
        pass

    def query(self, datatype):
        pass

    def get_actions(self, from_date, to_date):
        pass

    def get_horse_schedules(self, horse_id):
        pass

    def get_horse_people(self, horse_id, person_type=None):
        pass


class QuerySpec:
    DataType = ''
    Filters = {}
    Sorts = {}
    _doquery = None

    def __init__(self, datatype, doquery):
        self.DataType = datatype
        self._doquery = doquery

    def filter(self, prop, operator, value):
        queryable = False
        if prop == 'id':
            queryable = True
        elif self.DataType == 'schedule' and prop == 'horse_id':
            queryable = True
        elif self.DataType == 'association' and (prop == 'horse_id' or prop == 'person_id'):
            queryable = True
        elif self.DataType == 'action' and prop == 'horse_id':
            queryable = True
        self.Filters[prop] = (operator, value, queryable)
        return self

    def sort(self, prop, order='asc'):
        self.Sorts[prop] = order
        return self

    def go(self):
        return self._doquery(self)
