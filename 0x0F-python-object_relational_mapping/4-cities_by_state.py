#!/usr/bin/python3
"""select all cities"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    cur = db.cursor()
    sql = 'SELECT  cities.id, cities.name, states.name\
         FROM cities \
            INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC'
    cur.execute(sql)
    results = cur.fetchall()

    for result in results:
        print(result)
