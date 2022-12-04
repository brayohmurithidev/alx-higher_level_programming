#!/usr/bin/python3
"""
Insert record and output inserted
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
        tr = State(name="Louisiana")
        session.add(tr)

        try:
            session.flush()
            session.refresh(tr)
            if tr is not None:
                print("{}".format(tr.id))
        except Exception:
            session.rollback()
        finally:
            session.commit()

        session.close()
