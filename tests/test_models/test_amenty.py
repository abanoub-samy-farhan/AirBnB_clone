#!/usr/bin/python3
"""Module for testing Amenity class"""

import unittest
import pep8
from models.amenity import Amenity
from models.base_model import BaseModel

class TestAmenity(unittest.TestCase):
    """Test Amenity class implementation"""

    def test_doc_module(self):
        """Check if module has documentation"""
        self.assertGreater(len(Amenity.__doc__), 1)

    def test_pep8_conformance_amenity(self):
        """Check PEP8 conformance for models/amenity.py"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 style errors found.")

    def test_pep8_conformance_test_amenity(self):
        """Check PEP8 conformance for tests/test_models/test_amenity.py"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 style errors found.")

    def test_doc_constructor(self):
        """Check if constructor has documentation"""
        self.assertGreater(len(Amenity.__init__.__doc__), 1)

    def test_inheritance_and_attributes(self):
        """Validate inheritance and attributes types"""
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(Amenity, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(Amenity.name, str)

if __name__ == '__main__':
    unittest.main()
