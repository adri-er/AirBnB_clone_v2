#!/usr/bin/python3
"""
Module to store instances on the MySQL database
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import environ, getenv
print(getenv('HBNB_MYSQL_USER'))

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
            Session = sessionmaker(bind=DBStorage.__engine)
            DBStorage.__session = Session()
            delete_tables = DBStorage.__session.execute('DROP TABLE IF EXISTS cities, states')  # COmplete info
            DBStorage.__session.close()

    def all(self, cls=None):
        """  """
        from models.base_model import BaseModel
        from models.city import City
        from models.state import State

        Session = sessionmaker(bind=DBStorage.__engine)
        DBStorage.__session = Session()
        dictionary = {}

        if cls is None:
            result = DBStorage.__session.query(State, City).all()  # Complete classes
        else:
            result = DBStorage.__session.query(cls).all()

        for obj in result:
            dictionary[obj.__class__.__name__ + '.' + obj.id] = obj

        DBStorage.__session.close()

        return dictionary

    def new(self, obj):
        """  """
        Session = sessionmaker(bind=DBStorage.__engine)
        DBStorage.__session = Session()

        DBStorage.__session.add(obj)
        DBStorage.__session.commit()
        DBStorage.__session.close()

    def save(self):
        """  """
        Session = sessionmaker(bind=DBStorage.__engine)
        DBStorage.__session = Session()

        DBStorage.__session.commit()
        DBStorage.__session.close()

    def delete(self, obj=None):
        """ """
        if obj is not None:
            DBStorage.__session.delete(obj)

    def reload(self):
        """  """
        from models.base_model import BaseModel
        from models.city import City
        from models.state import State

        Base.metadata.create_all(DBStorage.__engine)
        Session = scoped_session(sessionmaker(bind=DBStorage.__engine,
                                              expire_on_commit=False))
        DBStorage.__session = Session()
