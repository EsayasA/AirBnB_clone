#!/usr/bin/python3
"""Explain review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class of review.

    Attributes:
        place_id (str): Place id.
        user_id (str): User id.
        text (str): text string.
    """

    place_id = ""
    user_id = ""
    text = ""
