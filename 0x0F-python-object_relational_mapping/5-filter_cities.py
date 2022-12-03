#!/usr/bin/python3
"""select all cities of a given state"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) >= 4:
        db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )

        cur = db.cursor()
        # SQL TO SELECT A LIST OF CITIES IN A GIVEN STATE
        sql = 'SELECT cities.name FROM cities INNER JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id ASC'
        state = (sys.argv[4],)
        cur.execute(sql, state)
        cities = cur.fetchall()
        print(", ".join(map(lambda x: x[0], cities)))
