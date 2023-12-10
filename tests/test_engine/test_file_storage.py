#!/usr/bin/python3
"""Test case FileStorage module"""

import unittest
import os
import json
import pep8
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel, Amenity, City, Place, Review, State, User


class TestFileStorage(unittest.TestCase):
    """Test FileStorage"""

    def setUp(self):
        """Sets up the class test"""
        self.models = [BaseModel(), Amenity(), City(), Place(), Review(), State(), User()]
        self.storage = FileStorage()
        self.storage.save()
        if not os.path.exists("file.json"):
            os.mknod("file.json")

    def tearDown(self):
        """Tears down the testing environment"""
        for model in self.models:
            del model
        del self.storage
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_pep8_FileStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0, "Fix pep8")

    def test_all(self):
        """Check the all method"""
        obj = self.storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, self.storage._FileStorage__objects)

    def test_storage_empty(self):
        """Check that the storage is not empty"""
        self.assertIsNotNone(self.storage.all())

    def test_storage_all_type(self):
        """Check the type of storage"""
        self.assertEqual(dict, type(self.storage.all()))

    def test_new(self):
        """Check the new method"""
        obj = self.storage.all()
        user = User()
        user.id = 1234
        user.name = "Julien"
        self.storage.new(user)
        key = "{}.{}".format(user.__class__.__name__, user.id)
        self.assertIsNotNone(obj[key])

    def test_check_json_loading(self):
        """Check if methods from Storage Engine work."""
        with open("file.json") as f:
            dic = json.load(f)
            self.assertEqual(isinstance(dic, dict), True)

    def test_file_existence(self):
        """Check if methods from Storage Engine work."""
        with open("file.json") as f:
            self.assertTrue(len(f.read()) > 0)

    def test_docstrings(self):
        """Check the docstrings of each function"""
        self.assertTrue(FileStorage.all.__doc__)
        self.assertTrue(hasattr(FileStorage, 'all'))
        self.assertTrue(FileStorage.new.__doc__)
        self.assertTrue(hasattr(FileStorage, 'new'))
        self.assertTrue(FileStorage.save.__doc__)
        self.assertTrue(hasattr(FileStorage, 'save'))
        self.assertTrue(FileStorage.reload.__doc__)
        self.assertTrue(hasattr(FileStorage, 'reload'))


if __name__ == '__main__':
    unittest.main()
