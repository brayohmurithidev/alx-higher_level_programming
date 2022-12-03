#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == '__main__':
    if len(sys.argv) >= 4:
        db = MySQLdb.connect(
            host='localhost',
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
        )
        cur = db.cursor()
        cur.execute(
            "SELECT * FROM states WHERE name IS NOT NULL AND LEFT(CAST(name AS BINARY), 1) = 'N' ORDER BY states.id;")
        records = cur.fetchall()
        for record in records:
            print(record)
        db.close()
