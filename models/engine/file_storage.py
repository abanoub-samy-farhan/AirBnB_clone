#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel



class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    @classmethod
    def all(self):
        """Return the dictionary __objects."""
        return self.__objects

    @classmethod
    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        obj_name = obj.__class__.__name__
        key = "{}.{}".format(obj_name, obj.id)
        self.__objects[key] = obj

    @classmethod
    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as f:
            json.dump(obj_dict, f)

    @classmethod
    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                nw_dict = json.load(f)
            for key, obj_data in nw_dict.items():
                cls_name = obj_data['__class__']
                print(cls_name)
                obj = obj_data(cls_name)(**obj_data)
                self.new(obj)
        except FileNotFoundError:
            pass
