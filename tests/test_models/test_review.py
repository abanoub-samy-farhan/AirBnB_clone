#!/usr/bin/python3
"""Module for testing Review class"""

import unittest
import pep8
from models.review import Review
from models.base_model import BaseModel

class TestReview(unittest.TestCase):
    """Test Review class implementation"""

    def test_doc_module(self):
        """Check if module has documentation"""
        self.assertGreater(len(Review.__doc__), 1)

    def test_pep8_conformance_review(self):
        """Check PEP8 conformance for models/review.py"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 style errors found.")

    def test_pep8_conformance_test_review(self):
        """Check PEP8 conformance for tests/test_models/test_review.py"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 style errors found.")

    def test_doc_constructor(self):
        """Check if constructor has documentation"""
        self.assertGreater(len(Review.__init__.__doc__), 1)

    def test_inheritance_and_attributes(self):
        """Validate inheritance and attribute types"""
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(Review, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(Review.place_id, str)
            self.assertIsInstance(Review.user_id, str)
            self.assertIsInstance(Review.text, str)

if __name__ == '__main__':
    unittest.main()
