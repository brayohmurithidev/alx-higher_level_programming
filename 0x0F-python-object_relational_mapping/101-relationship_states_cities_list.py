#!/usr/bin/python3
"""Fetch all data
"""
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(State).order_by(State.id.asc()).all()
    for result in results:
        print("{}: {}".format(result.id, result.name))
        for city in result.cities:
            print("\t{}: {}".format(city.id, city.name))

    session.close()
