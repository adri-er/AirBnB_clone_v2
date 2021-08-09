#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Class inherited from BaseModel that describes an Amenity """
    name = ""
