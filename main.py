import sql
import _mysql
from datetime import datetime

__author__ = 'nimnull'


def main():

    since = datetime.now()
    db = sql.Db(driver=_mysql, user='root', host='localhost')
    query = sql.SqlBuilder()
    query.Select(db.Users.id, db.Users.login).\
            From(db.Users).\
            Where(db.Users.last_login_time < since).\
            And(db.Users.login != 'admin')
    rows = query.FetchFrom(db)
    print dict((row.id, row.login) for row in rows)


if __name__ == '__main__':
    main()
  