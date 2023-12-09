#!/usr/bin/python3
"""Updating the JSON file with the reloaded data previously"""
from models.engine.file_storage import FileStorage


"""Reloading data from the JSON file"""
storage = FileStorage()
storage.reload()
