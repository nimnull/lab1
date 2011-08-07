
class SqlBuilder(object):
    
    def __init__(self):
        pass

    def Select(self, *args):
        self.select_columns = args
        return self

    def From(self, *args):
        self.from_tables = args
        return self

    def Where(self, *args):
        self.where_coluns = args
        return self

    def And(self, *args):
        self.and_columns = args
        return self

    def Delete(self):
        return self

    def Update(self):
        return self

    def FetchFrom(self, db):
        return db.fetchall()