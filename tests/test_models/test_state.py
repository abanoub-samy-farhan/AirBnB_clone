#!/usr/bin/python3
"""Module for testing State class"""

import unittest
import pep8
from models.state import State
from models.base_model import BaseModel

class TestState(unittest.TestCase):
    """Test State class implementation"""

    def test_doc_module(self):
        """Check if module has documentation"""
        self.assertGreater(len(State.__doc__), 1)

    def test_pep8_conformance_state(self):
        """Check PEP8 conformance for models/state.py"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 style errors found.")

    def test_pep8_conformance_test_state(self):
        """Check PEP8 conformance for tests/test_models/test_state.py"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_state.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 style errors found.")

    def test_doc_constructor(self):
        """Check if constructor has documentation"""
        self.assertGreater(len(State.__init__.__doc__), 1)

    def test_inheritance_and_attributes(self):
        """Validate inheritance and attribute types"""
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(State, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(State.name, str)

if __name__ == '__main__':
    unittest.main()
