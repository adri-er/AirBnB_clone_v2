#!/usr/bin/python3
"""Unistest of the Place class that inherits from Base_model"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """Class to test the Place class"""

    def __init__(self, *args, **kwargs):
        """ Inititializes an instance """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """Method to test the city_id attribute of the Place class"""
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """Method to test the user_id attribute of the Place class"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """Method to test the name attribute of the Place class"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """Method to test the description attribute of the Place class"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """Method to test the number_rooms attribute of the Place class"""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """Method to test the number_bathrooms attribute of the Place class"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """Method to test the max_guest attribute of the Place class"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """Method to test the price_by_night attribute of the Place class"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """Method to test the latitude attribute of the Place class"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """Method to test the longitude attribute of the Place class"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """Method to test the amenity_ids attribute of the Place class"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
