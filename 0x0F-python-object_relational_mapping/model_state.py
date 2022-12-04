from sqlalchemy import Column, String, Integer
# Import declarative base for the classes
from sqlalchemy.ext.declarative import declarative_base


# base to be used for the tables/ manage tables
Base = declarative_base()


# Define our mapped classes

class State(Base):
    __tablename__ = 'states'

    # Table properties
    idd = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    # A CONSTRUCTOR THAT IS OPRIONAL FOR PRETTIER OUTPUT
    def __init__(self, username, password):
        # self.user_id = user_id
        self.username = username
        self.password = password
