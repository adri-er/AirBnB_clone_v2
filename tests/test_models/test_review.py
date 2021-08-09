#!/usr/bin/python3
"""Unistest to test the Review class that inherits from Base_model"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """Class to test the Review class of the project"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """Method to test the place_id attribute of the Review class"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """Method to test the user_id attribute of the Review class"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """Method to test the text attribute of the Review class"""
        new = self.value()
        self.assertEqual(type(new.text), str)
