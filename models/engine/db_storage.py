#!/usr/bin/python3
"""
Module to store instances on the MySQL database
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import environ, getenv


class DBStorage:
    """Class"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize an instance"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(getenv('HBNB_MYSQL_USER'), getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'), getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            delete_tables = self.__session.execute('DROP TABLE IF EXISTS cities, states')  # COmplete info

    def all(self, cls=None):
        """  """
        from models.base_model import BaseModel
        from models.city import City
        from models.state import State

        dictionary = {}

        if cls is None:
            result = self.__session.query(State, City).all()  # Complete classes
        else:
            result = self.__session.query(cls).all()

        for obj in result:
            dictionary[obj.__class__.__name__ + '.' + obj.id] = obj

        return dictionary

    def new(self, obj):
        """  """
        self.__session.add(obj)

    def save(self):
        """  """
        self.__session.commit()

    def delete(self, obj=None):
        """ """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """  """
        from models.base_model import BaseModel, Base
        from models.city import City
        from models.state import State

        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()
