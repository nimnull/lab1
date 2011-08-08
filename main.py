import sql
from datetime import datetime


def main():
    since = datetime.now()
    db = sql.Db(user='root', host='localhost')
    query = sql.SqlBuilder()
    query.Select(db.Users.id, db.Users.login).\
            From(db.Users).\
            Where(db.Users.last_login_time < since).\
            And(db.Users.login != 'admin').And(db.Users.id != 123)
    rows = query.FetchFrom(db)
    print dict((row.id, row.login) for row in rows)


if __name__ == '__main__':
    main()
  