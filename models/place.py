#!/usr/bin/python3
""" Place Module for HBNB project """
from models import amenity
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from models import storage
from models.review import Review
from models.amenity import Amenity
import os

place_amenity = Table("place_amenity", Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'), PrimaryKey=True),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), PrimaryKey=True))


class Place(BaseModel, Base):
    """ Class inherited from BaseModel that describes a Place """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    user = relationship("User", back_populates="places")

    cities = relationship("City", back_populates="places")

    reviews = relationship('Review', back_populates="place",
                           single_parent=True,
                           cascade="all, delete, delete-orphan")

    amenities = relationship("Amenity", secondary=place_amenity, viewonly=False)

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':

        @property
        def reviews(self):
            """ Getter reviews """
            list_reviews = []
            for review in list(storage.all(Review).values()):
                if self.id == review.place_id:
                    list_reviews.append(review)
            return list_reviews

        @property
        def amenities(self):
            """ Getter amenities """
            list_amenities = []
            dict_amenities = storage.all(Amenity)

            for id_amenity in self.amenity_ids:
                key = "Amenity. " + id_amenity
                if key in dict_amenities.keys():
                    list_amenities.append(dict_amenities[key])
            return list_amenities

        @amenities.setter
        def amenities(self, obj=None):
            """ Setter amenities """
            if obj is not None and obj.__class__.__name__ == 'Amenity':
                self.amenity_ids.append(obj.id)
