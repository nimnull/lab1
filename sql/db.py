import MySQLdb
from MySQLdb.cursors import DictCursor

class Db(object):
    tables = {}
    
    def __init__(self, **kwargs):
        self.db = MySQLdb.connect(**kwargs)
        self.cursor = self.db.cursor(DictCursor)


    def __getattr__(self, item):
        if item not in self.tables:
            self.tables[item] = DbTable(item)
        return self.tables[item]

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
            self.fields[item] = DbField(item)
        return self.fields[item]



class DbField(DbItem):

    def __eq__(self, other):
        print "eq %s" % other
        return hash(self)

    def __ne__(self, other):
        print "ne %s" % other
        return hash(self)

    def __le__(self, other):
        print "le %s" % other
        return hash(self)

    def __ge__(self, other):
        print "ge %s" % other
        return hash(self)

    def __lt__(self, other):
        print "lt %s" % other
        return hash(self)

    def __gt__(self, other):
        print "gt %s" % other
        return hash(self)


class DbResponse(object):

    def __init__(self, row_dict):
        self.row_dict = row_dict

    def __getattr__(self, item):
        if item not in self.__dict__:
            return self.row_dict.get(item, None)
