#!/usr/bin/python3
"""Unistest to tet the User class that inherist from base_model"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """Class to test the User class of the project"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """Method to test the first_name attibute of the User class"""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """Method to test the last_name attibute of the User class"""
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """Method to test the email attibute of the User class"""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """Method to test the password attibute of the User class"""
        new = self.value()
        self.assertEqual(type(new.password), str)
