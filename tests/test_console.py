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
    this class test HBNBCommand class and its behavior
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

    def test_aa_create(self):
        """ create tests """
        no_stdout = " > /dev/null 2>&1"
        run("rm file.json " + no_stdout)
        run("echo 'create State' | ./console.py" + no_stdout)
        run("echo 'all' | ./console.py" + no_stdout)
        with open("file.json", 'r') as f:
            temp = json.load(f)
        self.assertTrue(temp)

    def test_ab_create(self):
        """ create tests """
        no_stdout = " > /dev/null 2>&1"
        run("rm file.json " + no_stdout)
        run('echo create State name="California" | ./console.py' + no_stdout)
        run("echo 'all' | ./console.py" + no_stdout)
        with open("file.json", 'r') as f:
            temp = json.load(f)
        self.assertTrue(temp)

    def test_ac_create(self):
        """ create tests """
        no_stdout = " > /dev/null 2>&1"
        run("rm file.json " + no_stdout)
        command = 'echo create City state_id="1" name="San_Francisco" '
        command = command + '| ./console.py '
        run(command + no_stdout)
        run("echo 'all' | ./console.py" + no_stdout)
        with open("file.json", 'r') as f:
            temp = json.load(f)
        self.assertTrue(temp)

    def test_ac_create(self):
        """ create tests """
        no_stdout = " > /dev/null 2>&1"
        run("rm file.json " + no_stdout)
        command = 'echo create City state_id="1" name="San_Francisco" '
        command = command + '| ./console.py '
        run(command + no_stdout)
        run("echo 'all' | ./console.py" + no_stdout)
        with open("file.json", 'r') as f:
            temp = json.load(f)
        self.assertTrue(temp)

    def test_create_state(self):
        """ create tests """
        no_stdout = " > /dev/null 2>&1"
        command = 'echo "create State name="California""'
        sp_1 = " HBNB_MYSQL_USER=hbnb_test HBNB_MYSQL_PWD=hbnb_test_pwd "
        sp_2 = "HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_test_db "
        sp_3 = "HBNB_TYPE_STORAGE=db HBNB_ENV=test "
        command = command + '|{}{}{}./console.py '.format(sp_1, sp_2, sp_3)
        run(command + no_stdout)

        command = 'echo "SELECT COUNT(*) FROM states"'
        sp_1 = " HBNB_MYSQL_USER=hbnb_test HBNB_MYSQL_PWD=hbnb_test_pwd "
        sp_2 = "HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_test_db "
        sp_3 = "HBNB_TYPE_STORAGE=db"
        command = command + '|{}{}{}./console.py '.format(sp_1, sp_2, sp_3)
        std_out = StringIO()
        sys.stdout = std_out
        run(command + no_stdout)
        output = std_out.getvalue()
        self.assertEqual(output, 1)

    def test_create_city(self):
        """ create tests """
        no_stdout = " > /dev/null 2>&1"
        command = 'echo "create State name="California" id=34"'
        sp_1 = " HBNB_MYSQL_USER=hbnb_test HBNB_MYSQL_PWD=hbnb_test_pwd "
        sp_2 = "HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_test_db "
        sp_3 = "HBNB_TYPE_STORAGE=db HBNB_ENV=test "
        command = command + '|{}{}{}./console.py '.format(sp_1, sp_2, sp_3)
        run(command + no_stdout)

        no_stdout = " > /dev/null 2>&1"
        command = 'echo "create City state_id="34" name="San Francisco""'
        sp_1 = " HBNB_MYSQL_USER=hbnb_test HBNB_MYSQL_PWD=hbnb_test_pwd "
        sp_2 = "HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_test_db "
        sp_3 = "HBNB_TYPE_STORAGE=db HBNB_ENV=test "
        command = command + '|{}{}{}./console.py '.format(sp_1, sp_2, sp_3)
        run(command + no_stdout)

        command = 'echo "SELECT COUNT(*) FROM cities"'
        sp_1 = " HBNB_MYSQL_USER=hbnb_test HBNB_MYSQL_PWD=hbnb_test_pwd "
        sp_2 = "HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_test_db "
        sp_3 = "HBNB_TYPE_STORAGE=db"
        command = command + '|{}{}{}./console.py '.format(sp_1, sp_2, sp_3)
        std_out = StringIO()
        sys.stdout = std_out
        run(command + no_stdout)
        output = std_out.getvalue()
        self.assertEqual(output, 1)
