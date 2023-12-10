#!/usr/bin/python3
"""Module for testing User class"""

import unittest
import pep8
from models.user import User
from models.base_model import BaseModel

class TestUser(unittest.TestCase):
    """Test User class implementation"""

    def test_doc_module(self):
        """Check if module has documentation"""
        self.assertGreater(len(User.__doc__), 1)

    def test_pep8_conformance_user(self):
        """Check PEP8 conformance for models/user.py"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 style errors found.")

    def test_pep8_conformance_test_user(self):
        """Check PEP8 conformance for tests/test_models/test_user.py"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_user.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 style errors found.")

    def test_doc_constructor(self):
        """Check if constructor has documentation"""
        self.assertGreater(len(User.__init__.__doc__), 1)

    def test_inheritance_and_attributes(self):
        """Validate inheritance and attribute types"""
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(User, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(User.email, str)
            self.assertIsInstance(User.password, str)
            self.assertIsInstance(User.first_name, str)
            self.assertIsInstance(User.last_name, str)

if __name__ == '__main__':
    unittest.main()
