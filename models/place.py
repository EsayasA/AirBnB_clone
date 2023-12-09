#!/usr/bin/python3
"""Explaines class of Place."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Class of a place.

    Attributes:
        city_id (str): city id.
        user_id (str): User id.
        name (str): name.
        description (str): description.
        number_rooms (int): number of rooms.
        number_bathrooms (int): number of bathrooms.
        max_guest (int): maximum number of peoples.
        price_by_night (int): price at night.
        latitude (float): latitude.
        longitude (float): longitude.
        amenity_ids (list): list id.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
