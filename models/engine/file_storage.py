#!/usr/bin/python3
"""This module defines the FileStorage class"""

import json


class FileStorage:
    """
    manages serialization and deserialization of objects to/from a JSON file
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = {key: value.to_dict()
                    for key, value in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects (if the file exists)"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                obj_dict = json.load(f)
                from models.base_model import BaseModel
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    cls = eval(class_name)
                    new_obj = cls(**value)
                    self.new(new_obj)
        except FileNotFoundError:
            pass
