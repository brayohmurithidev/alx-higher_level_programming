#!/usr/bin/python3
"""Filter by user input"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) >= 4:
        db = MySQLdb.connect(
            host='localhost',
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
        )
        cursor = db.cursor()
        sql = "SELECT * FROM states WHERE name= %s"
        name = (sys.argv[4],)
        cursor.execute(sql, name)
        results = cursor.fetchall()
        for result in results:
            print(result)
