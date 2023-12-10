#!/usr/bin/python3
"""This explaines unittests for models/place.py.

Unittest classes:
    TestPlace_Esayas
    TestPlace_Aregawi
    TestPlace_Teklay
"""
import unittest
import models
import os
from datetime import datetime
from models.place import Place
from time import sleep

class TestPlace_Esayas(unittest.TestCase):
    """Unittests to test."""

    def test_empty_instantiates(self):
        self.assertEqual(Place, type(Place()))

    def test_new_stored_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_is_public_str(self):
        self.assertEqual(str, type(Place().id))

    def test_created_at_time(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_time(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_city_class_attribute(self):
        pla = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(pla))
        self.assertNotIn("city_id", pla.__dict__)

    def test_user_id_is_public_attribute(self):
        pla = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(pla))
        self.assertNotIn("user_id", pla.__dict__)

    def test_name_public_class(self):
        pla = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(pla))
        self.assertNotIn("name", pla.__dict__)

    def test_public_class_attribute(self):
        pla = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(pla))
        self.assertNotIn("desctiption", pla.__dict__)

    def test_rooms_public_class_attribute(self):
        pla = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(pla))
        self.assertNotIn("number_rooms", pla.__dict__)

    def test_bathrooms_class_attribute(self):
        pla = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(pla))
        self.assertNotIn("number_bathrooms", pla.__dict__)

    def test_max_guest_class_attribute(self):
        pla = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(pla))
        self.assertNotIn("max_guest", pla.__dict__)

    def test_price_class_attribute(self):
        pla = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(pla))
        self.assertNotIn("price_by_night", pla.__dict__)

    def test_latitude_class_attribute(self):
        pla = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(pla))
        self.assertNotIn("latitude", pla.__dict__)

    def test_longitude_class_attribute(self):
        pla = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(pla))
        self.assertNotIn("longitude", pla.__dict__)

    def test_amenity_cclass_attribute(self):
        pla = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(pla))
        self.assertNotIn("amenity_ids", pla.__dict__)

    def test_twounique_ids(self):
        pla1 = Place()
        pla2 = Place()
        self.assertNotEqual(pla1.id, pla2.id)

    def test_twoplaces_created_at(self):
        pla1 = Place()
        sleep(0.05)
        pla2 = Place()
        self.assertLess(pla1.created_at, pla2.created_at)

    def test_two_places_dupdated_at(self):
        pla1 = Place()
        sleep(0.05)
        pla2 = Place()
        self.assertLess(pla1.updated_at, pla2.updated_at)

    def test_str_represente(self):
        dat = datetime.today()
        dat_repr = repr(dat)
        pla = Place()
        pla.id = "123456"
        pla.created_at = pla.updated_at = dat
        plstr = pla.__str__()
        self.assertIn("[Place] (123456)", plstr)
        self.assertIn("'id': '123456'", plstr)
        self.assertIn("'created_at': " + dat_repr, plstr)
        self.assertIn("'updated_at': " + dat_repr, plstr)

    def test_args_notused(self):
        pla = Place(None)
        self.assertNotIn(None, pla.__dict__.values())

    def test_instant_withkwargs(self):
        dat = datetime.today()
        dat_iso = dat.isoformat()
        pla = Place(id="345", created_at=dat_iso, updated_at=dat_iso)
        self.assertEqual(pla.id, "345")
        self.assertEqual(pla.created_at, dat)
        self.assertEqual(pla.updated_at, dat)

    def test_instant_with_out_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)


class TestPlace_Aregawi(unittest.TestCase):
    """Unittests to test class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_onesave(self):
        pla = Place()
        sleep(0.05)
        first_updated_at = pla.updated_at
        pla.save()
        self.assertLess(first_updated_at, pla.updated_at)

    def test_twosaves(self):
        pla = Place()
        sleep(0.05)
        first_updated_at = pla.updated_at
        pla.save()
        second_updated_at = pla.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        pla.save()
        self.assertLess(second_updated_at, pla.updated_at)

    def test_save_with_arg(self):
        pla = Place()
        with self.assertRaises(TypeError):
            pla.save(None)

    def test_updates_file(self):
        pla = Place()
        pla.save()
        plid = "Place." + pla.id
        with open("file.json", "r") as f:
            self.assertIn(plid, f.read())


class TestPlace_Teklay(unittest.TestCase):
    """Unittests to test."""

    def test_to_dictype(self):
        self.assertTrue(dict, type(Place().to_dict()))

    def test_to_dict_correct_keys(self):
        pla = Place()
        self.assertIn("id", pla.to_dict())
        self.assertIn("created_at", pla.to_dict())
        self.assertIn("updated_at", pla.to_dict())
        self.assertIn("__class__", pla.to_dict())

    def test_to_dict_attributes(self):
        pla = Place()
        pla.middle_name = "Holberton"
        pla.my_number = 98
        self.assertEqual("Holberton", pla.middle_name)
        self.assertIn("my_number", pla.to_dict())

    def test_to_dict_datetime(self):
        pla = Place()
        pla_dict = pla.to_dict()
        self.assertEqual(str, type(pla_dict["id"]))
        self.assertEqual(str, type(pla_dict["created_at"]))
        self.assertEqual(str, type(pla_dict["updated_at"]))

    def test_to_output(self):
        dat = datetime.today()
        pla = Place()
        pla.id = "123456"
        pla.created_at = pla.updated_at = dat
        tdict = {
            'id': '123456',
            '__class__': 'Place',
            'created_at': dat.isoformat(),
            'updated_at': dat.isoformat(),
        }
        self.assertDictEqual(pla.to_dict(), tdict)

    def test_contrast_to_dict(self):
        pla = Place()
        self.assertNotEqual(pla.to_dict(), pla.__dict__)

    def test_to_dict_argument(self):
        pla = Place()
        with self.assertRaises(TypeError):
            pla.to_dict(None)


if __name__ == "__main__":
    unittest.main()
