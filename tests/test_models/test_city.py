#!/usr/bin/python3
"""Unittest module of the City class that inhrits from Base_model"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """Class test_city to test the City class"""

    def __init__(self, *args, **kwargs):
        """ Inititializes an instance """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Method to test the state_id attribute of the City class"""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """Method to test the name attribute of the City class"""
        new = self.value()
        self.assertEqual(type(new.name), str)
