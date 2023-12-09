#!/usr/bin/python3
"""Explaines city class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Class of a city.

    Attributes:
        state_id (str): id.
        name (str): name.
    """

    state_id = ""
    name = ""
