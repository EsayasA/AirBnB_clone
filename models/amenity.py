#!/usr/bin/python3
"""Explain amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent an amenity.

    Attributes:
        name (str): name with string.
    """

    name = ""
