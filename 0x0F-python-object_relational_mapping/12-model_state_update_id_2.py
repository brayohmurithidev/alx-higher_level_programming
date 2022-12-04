#!/usr/bin/python3
"""
Update a record
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

        record = session.query(State).filter(State.id == 2)
        record.update({State.name: 'New Mexico'})
        session.commit()

        session.close()
