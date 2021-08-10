#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from models import storage
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    cities = relationship(
        "City",
        backref="states",
        cascade="all, delete, delete-orphan"
    )
    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """ Getter cities """
            list_city = []
            for city in list(storage.all(City).values()):
                if self.id == city.state_id:
                    list_city.append(city)
            return list_city
