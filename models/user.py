#!/usr/bin/python3
"""Represent User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Define a User.

    Attributes:
        email (str): email.
        password (str): password.
        first_name (str): first name.
        last_name (str): last name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
