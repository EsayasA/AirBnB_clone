#!/usr/bin/python3
"""Define BaseModel class."""
from uuid import uuid4
import models
from datetime import datetime


class BaseModel:
    """Represent the basemodel of this project."""

    def __init__(self, *args, **kwargs):
        """Init function.

        Args:
            *args (any): argument.
            **kwargs (dict): arguments with key and value pairs.
        """
        formm = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for ke, va in kwargs.items():
                if ke == "created_at" or ke == "updated_at":
                    self.__dict__[ke] = datetime.strptime(va, formm)
                else:
                    self.__dict__[ke] = va
        else:
            models.storage.new(self)

    def save(self):
        """updates the public instance attribute updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance """
        redic = self.__dict__.copy()
        redic["created_at"] = self.created_at.isoformat()
        redic["updated_at"] = self.updated_at.isoformat()
        redic["__class__"] = self.__class__.__name__
        return redic

    def __str__(self):
        """should print."""
        classname = self.__class__.__name__
        return "[{}] ({}) {}".format(classname, self.id, self.__dict__)
