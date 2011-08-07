
class Db(object):
    
    def __init__(self, **kwargs):
        self.driver = kwargs.pop('driver')
        self.db = self.driver.connect(**kwargs)


    def __getattr__(self, item):
        if item not in self.__dict__:
            self.__dict__[item] = DbTable(item)
        else:
            return __dict__[item]


class DbItem(object):

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name



class DbTable(DbItem):

    def __getattr__(self, item):
        if item not in self.__dict__:
            self.__dict__[item] = DbField(item)
        else:
            return __dict__[item]



class DbField(DbItem):

    def __eq__(self, other):
        pass

    def __ne__(self, other):
        pass

    def __cmp__(self, other):
        pass