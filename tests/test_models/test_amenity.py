#!/usr/bin/python3
"""Unittest module to test the amenity class"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """Class to test the amenity class that inherits from test_basemodel"""

    def __init__(self, *args, **kwargs):
        """ Inititializes an instance """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """Method to test the amenity class"""
        new = self.value()
        self.assertEqual(type(new.name), str)
