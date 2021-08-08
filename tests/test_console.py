#!/usr/bin/python3
'''
    module documentation
'''
import unittest
from models.base_model import BaseModel
import os
import sys
from console import HBNBCommand
from io import StringIO


class TestHBNBCommand(unittest.TestCase):
    """
    this class test HBNBCommand class and your behavior
    """
    def setUp(self) -> None:
        return super().setUp()

    def out_test(self, func, arg, expect):
        """Axiliar function to test some commands of the console"""
        std_out = StringIO()
        sys.stdout = std_out
        func(arg)
        output = std_out.getvalue()
        self.assertEqual(output, expect + '\n')
        return output
