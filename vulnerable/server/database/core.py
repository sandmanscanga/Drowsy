#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from . import *
from .config import _CREDS
from .samples import Samples


def reinit_database(total_users=250):
    try:
        db = MySQLdb.connect(**_CREDS)
        c = db.cursor()
        c.execute("DROP TABLE IF EXISTS users;")
        c.execute("""
CREATE TABLE users(
    id INTEGER NOT NULL PRIMARY KEY,
    first_name VARCHAR(1000) NOT NULL,
    last_name VARCHAR(1000) NOT NULL,
    password VARCHAR(1000) NOT NULL
);
        """)
        for user in Samples(sample_size=total_users):
            c.execute("INSERT INTO users VALUES %s;" % user)
        db.commit()
    except MySQLdb._exceptions.OperationalError as error:
        sys.stderr.write(str(error))
        sys.stderr.write("\n")
        sys.stderr.flush()
        sys.exit(1)


def search_database(query, by_name=True):
    try:
        db = MySQLdb.connect(**_CREDS)
        c = db.cursor()
        if by_name:
            c.execute("SELECT id, first_name, last_name FROM users WHERE last_name LIKE '%s%%';" % query)
        else:
            c.execute("SELECT id, first_name, last_name FROM users WHERE id=%s AND id IS NOT NULL;" % query)
    except MySQLdb._exceptions.OperationalError as error:
        sys.stderr.write(str(error))
        sys.stderr.write("\n")
        sys.stderr.flush()
        sys.exit(1)
    else:
        rows = c.fetchall()
        sys.stderr.write("Results: %s\n" % repr(rows))
        sys.stderr.flush()
        return rows
