import MySQLdb
from MySQLdb.cursors import DictCursor

class Db(object):
    tables = {}
    
    def __init__(self, **kwargs):
        self.db = MySQLdb.connect(**kwargs)
        self.cursor = self.db.cursor(DictCursor)


    def __getattr__(self, item):
        item_lower = item.lower()
        if item not in self.tables:
            self.tables[item_lower] = DbTable(item_lower)
        return self.tables[item_lower]

    def fetchall(self):
        #self.cursor.execute()
        return [DbResponse({'id':1, 'login': 'test'}),]


class DbItem(object):

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name



class DbTable(DbItem):
    fields = {}

    def __getattr__(self, item):
        if item not in self.__dict__:
            self.fields[item] = DbField(self, item)
        return self.fields[item]



class DbField(DbItem):

    def __init__(self, table, name):
        self.table = table
        super(DbField, self).__init__(name)

    def __eq__(self, other):
        return self, '=', other

    def __ne__(self, other):
        return self, '!=', other

    def __le__(self, other):
        return self, '<=', other

    def __ge__(self, other):
        return self, '>=', other

    def __lt__(self, other):
        return self, '<', other

    def __gt__(self, other):
        return self, '>', other


class DbResponse(object):

    def __init__(self, row_dict):
        self.row_dict = row_dict

    def __getattr__(self, item):
        if item not in self.__dict__:
            return self.row_dict.get(item, None)
