#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        """Initialize the storage system and load existing data."""
        self.reload()

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return FileStorage.__objects
        else:
            filtered_dict = {}
            for key, obj in FileStorage.__objects.items():
                if isinstance(obj, cls):
                    filtered_dict[key] = obj
            return filtered_dict

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        try:
            with open(FileStorage.__file_path, 'w') as f:
                temp = {
                    k: v.to_dict()
                    for k, v in FileStorage.__objects.items()
                }
                json.dump(temp, f)
        except Exception as e:
            print(f"Error saving to file: {e}")

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }

        try:
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    cls_name = val['__class__']
                    cls = classes[cls_name]
                    self.new(cls(**val))
        except FileNotFoundError:
            print("No file found, starting with an empty storage")
        except json.JSONDecodeError:
            print("Error decoding JSON from file")
        except Exception as e:
            print(f"Error loading from file: {e}")

    def delete(self, obj=None):
        """Deletes obj from __objects if it's inside"""
        if obj is not None:
            key = f"{obj.__class__.__name__}.{obj.id}"
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]
