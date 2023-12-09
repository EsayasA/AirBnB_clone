#!/usr/bin/python3
"""Explaines the drived class of FileStorage."""
from models.base_model import BaseModel
import json
from models.state import State
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Defines storage engine.

    Attributes:
        __file_path (str): path of the file.
        __objects (dict): dictionary.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        octnam = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(octnam, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odic = FileStorage.__objects
        objdic = {obj: odic[obj].to_dict() for obj in odic.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdic, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists otherwise do nothing."""
        try:
            with open(FileStorage.__file_path) as f:
                objdic = json.load(f)
                for o in objdic.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
