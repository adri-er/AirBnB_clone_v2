#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ Class inherited from BaseModel that describes a State """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='states', cascade='all, delete-orphan')
    else:
        from models.engine.file_storage import FileStorage
        cities = []
        for key, value in FileStorage.__objects.items():
            cls_id = key.split('.')
            cls = cls_id[0]

            if cls == 'City' and value.state_id == self.id:
                cities.append(value)
