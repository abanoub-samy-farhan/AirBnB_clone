#!/usr/bin/python3

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class"""

    def __init__(self, *args, **kwargs):
        """Initialize Amenity args with BaseModel args"""
        super().__init__(*args, **kwargs)
        self.name = ""
