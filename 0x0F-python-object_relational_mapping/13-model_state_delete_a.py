#!/usr/bin/python3
"""
Delete all records with letter a
"""
import sys
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine


if __name__ == "__main__":
    if len(sys.argv) >= 4:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

        Base.metadata.create_all(engine)
        Session = sessionmaker(engine)
        session = Session()

        recordToDelete = session.query(State).filter(
            State.name.like('%a%'))
        for record in recordToDelete:
            session.delete(record)

        session.commit()
        session.close()
