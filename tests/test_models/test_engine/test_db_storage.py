#!/usr/bin/python3
"""
Unistest to tste the command line console to manage the web site
"""
import unittest

from sqlalchemy.sql.expression import select
from models.base_model import BaseModel
import os
import sys
from console import HBNBCommand
from io import StringIO
import json
import cmd
import pep8
from unittest.mock import patch
from io import StringIO
import json

run = os.system


class TestHBNBCommand(unittest.TestCase):
    """
    this class test sql storage
    """

    def setUp(self) -> None:
        """Test module to test the console and its functionality"""
        return super().setUp()

    def out_test(self, func, arg, expect):
        """Axiliar function to test some commands of the console"""
        std_out = StringIO()
        sys.stdout = std_out
        func(arg)
        output = std_out.getvalue()
        self.assertEqual(output, expect + '\n')
        return output

    def test_docstring(self):
        """docstring"""
        self.assertIsNotNone(HBNBCommand.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)

    def test_pep8(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0)
