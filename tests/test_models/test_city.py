#!/usr/bin/python3
"""Module for testing City class"""

import unittest
import pep8
from models.city import City
from models.base_model import BaseModel

class TestCity(unittest.TestCase):
    """Test City class implementation"""

    def test_doc_module(self):
        """Check if module has documentation"""
        self.assertGreater(len(City.__doc__), 1)

    def test_pep8_conformance_city(self):
        """Check PEP8 conformance for models/city.py"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 style errors found.")

    def test_pep8_conformance_test_city(self):
        """Check PEP8 conformance for tests/test_models/test_city.py"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_city.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 style errors found.")

    def test_doc_constructor(self):
        """Check if constructor has documentation"""
        self.assertGreater(len(City.__init__.__doc__), 1)

    def test_inheritance_and_attributes(self):
        """Validate inheritance and attribute types"""
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(City, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(City.name, str)
            self.assertIsInstance(City.state_id, str)

if __name__ == '__main__':
    unittest.main()
