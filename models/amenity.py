#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models.place import place_amenity
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """ Class inherited from BaseModel that describes an Amenity """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenity = relationship("Place", secondary=place_amenity)
