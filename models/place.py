#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy.sql.sqltypes import Float
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship

class Place(BaseModel):
    """ Class inherited from BaseModel that describes a Place """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []

    user = relationship("User", back_populates="places",
                        cascade="all, delete, delete-orphan")

    cities = relationship("City", back_populates="places",
                        cascade="all, delete, delete-orphan")
