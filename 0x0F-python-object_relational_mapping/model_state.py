#!/usr/bin/python3
from sqlalchemy import Column, String, Integer
# Import declarative base for the classes
from sqlalchemy.ext.declarative import declarative_base


# base to be used for the tables/ manage tables
Base = declarative_base()


# Define our mapped classes

class State(Base):
    __tablename__ = 'states'

    # Table properties
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
