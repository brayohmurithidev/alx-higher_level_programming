#!/usr/bin/python3
"""
Selects states with a
"""
import sys
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()
    records = session.query(State).filter(State.name.like('%a%'))
    for record in records:
        print("{}: {}".format(record.id, record.name))

    session.close()
