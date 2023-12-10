#!/usr/bin/python3
"""Module for testing Place class"""

import unittest
import pep8
from models.place import Place
from models.base_model import BaseModel

class TestPlace(unittest.TestCase):
    """Test Place class implementation"""

    def test_doc_module(self):
        """Check if module has documentation"""
        self.assertGreater(len(Place.__doc__), 1)

    def test_pep8_conformance_place(self):
        """Check PEP8 conformance for models/place.py"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 style errors found.")

    def test_pep8_conformance_test_place(self):
        """Check PEP8 conformance for tests/test_models/test_place.py"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_place.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 style errors found.")

    def test_doc_constructor(self):
        """Check if constructor has documentation"""
        self.assertGreater(len(Place.__init__.__doc__), 1)

    def test_inheritance_and_attributes(self):
        """Validate inheritance and attribute types"""
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(Place, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(Place.city_id, str)
            self.assertIsInstance(Place.user_id, str)
            self.assertIsInstance(Place.name, str)
            self.assertIsInstance(Place.description, str)
            self.assertIsInstance(Place.number_rooms, int)
            self.assertIsInstance(Place.number_bathrooms, int)
            self.assertIsInstance(Place.max_guest, int)
            self.assertIsInstance(Place.price_by_night, int)
            self.assertIsInstance(Place.latitude, float)
            self.assertIsInstance(Place.longitude, float)
            self.assertIsInstance(Place.amenity_ids, list)

if __name__ == '__main__':
    unittest.main()
