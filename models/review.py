#!/usr/bin/python3
"""Explain review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class of review.

    Attributes:
        place_id (str): id of the place.
        user_id (str): id of the user.
        text (str): text string.
    """

    place_id = ""
    user_id = ""
    text = ""
