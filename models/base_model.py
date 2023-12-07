#!/usr/bin/python3
"""Base Model for AirBnB project"""
from datetime import datetime
import uuid


class BaseModel:
    """BaseModel class instances and methods"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updadted_at = datetime.now()

    def __str__(self):
        """returning a string defining the class"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, dict(self.__dict__))

    def to_dict(self):
        """To return a dict containing all the variables and class name"""
        instance_dict = self.__dict__.copy()
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updadted_at.isoformat()
        return instance_dict

    def save(self):
        """Save the file"""
        self.updadted_at = datetime.now()