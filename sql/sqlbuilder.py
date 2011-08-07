from exception import SqlBuilderException

class SqlBuilder(object):
    
    def __init__(self):
        pass

    def Select(self, *args):
        if getattr(self, 'select_columns', False):
            raise SqlBuilderException('You have already defined columns to select from')
        self.select_columns = ["%s.%s" % (c.table, c.name) for c in args]
        return self

    def From(self, *args):
        if getattr(self, 'from_tables', False):
            raise SqlBuilderException('You have already defined FROM table')
        if not len(self.select_columns):
            raise SqlBuilderException('From used before Select')
        self.from_tables = args
        return self

    def Where(self, *args):
        if not len(self.select_columns):
            raise SqlBuilderException('Where used before Select')
        if not len(self.from_tables):
            raise SqlBuilderException('Where used before From')
        self.conditions = args
        return self

    def And(self, *args):
        self.conditions += args
        return self

    def Delete(self):
        return self

    def Update(self):
        return self

    def FetchFrom(self, db):
        return db.fetchall()