#!/usr/bin/python3
"""Base Model for AirBnB project"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """BaseModel class instances and methods"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            dictionary_mod = self.__dict__
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    time_form = datetime.strptime(kwargs[key],
                                                  "%Y-%m-%dT%H:%M:%S.%f")
                    dictionary_mod[key] = time_form
                elif key != "__class__":
                    dictionary_mod[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """returning a string defining the class"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, dict(self.__dict__))

    def to_dict(self):
        """To return a dict containing all the variables and class name"""
        instance_dict = self.__dict__.copy()
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()
        return instance_dict

    def save(self):
        """Save the file"""
        self.updated_at = datetime.now()
        models.storage.save()
