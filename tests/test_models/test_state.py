#!/usr/bin/python3
"""Unistest to test the User class that inherits from base_model"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """Class to test the State class of the project"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """Method to test the name attibute of the State class"""
        new = self.value()
        self.assertEqual(type(new.name), str)
