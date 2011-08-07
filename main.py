from MySQLdb.cursors import DictCursor
import sql
import MySQLdb
from datetime import datetime

__author__ = 'nimnull'


def main():

    since = datetime.now()
    db = sql.Db(user='root', host='localhost')
    query = sql.SqlBuilder()
    query.Select(db.Users.id, db.Users.login).\
            From(db.Users).\
            Where(db.Users.last_login_time < since).\
            And(db.Users.login != 'admin')
    rows = query.FetchFrom(db)
    print dict((row.id, row.login) for row in rows)


if __name__ == '__main__':
    main()
  