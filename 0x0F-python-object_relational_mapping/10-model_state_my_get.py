#!/usr/bin/python3
"""
Search with state argument given
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
        state_name = sys.argv[4]
        result = session.query(State).filter(State.name == state_name).first()
    if result is not None:
        print(result.id)
    else:
        print("Not found")

        session.close()
