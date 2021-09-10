#!/usr/bin/python3
"""
Module to store instances on the MySQL database.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import environ, getenv


class DBStorage:
    """Class that represents SQL storage"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize an instance"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            from models.base_model import Base
            Base.metadata.drop_all()

    def all(self, cls=None):
        """ Prints all the instances specified, or not """
        from models.base_model import BaseModel
        from models.city import City
        from models.state import State
        from models.user import User
        from models.place import Place
        from models.review import Review
        from models.amenity import Amenity

        dictionary = {}

        if cls is None:
            result = self.__session.query(
                State, City, User, Place, Review, Amenity).all()
        # AGREGAR clase
        else:
            result = self.__session.query(cls).all()

        for obj in result:
            dictionary[obj.__class__.__name__ + '.' + obj.id] = obj

        return dictionary

    def new(self, obj):
        """ Adds an instance to the program """
        self.__session.add(obj)

    def save(self):
        """ Adds the instance to the SQL database """
        self.__session.commit()

    def delete(self, obj=None):
        """ Removes and instance from the database """
        if obj is not None:
            self.__session.delete(obj)
        self.save()

    def reload(self):
        """ Reloads data from the database """
        from models.base_model import BaseModel, Base
        from models.city import City
        from models.state import State
        from models.user import User
        from models.place import Place
        from models.review import Review
        from models.amenity import Amenity

        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()

    def close(self):
        """ Closes session of mysql """
        self.__session.remove()
