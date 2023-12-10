#!/usr/bin/python3
"""This explaines unittests for models/city.py.

Unittest classes:
    TestCity_Esayas
    TestCity_Aregawi
    TestCity_Teklay
"""
import unittest
import models
import os
from datetime import datetime
from time import sleep
from models.city import City


class TestCity_Esayas(unittest.TestCase):
    """Unittests to test class of City."""

    def test_no_argument(self):
        self.assertEqual(City, type(City()))

    def test_new_instance_storedin(self):
        self.assertIn(City(), models.storage.all().values())

    def test_is_publstr(self):
        self.assertEqual(str, type(City().id))

    def test_created_time(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_time(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_state_attribute(self):
        cty = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(cty))
        self.assertNotIn("state_id", cty.__dict__)

    def test_public_class_attribute(self):
        cty = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(cty))
        self.assertNotIn("name", cty.__dict__)

    def test_two_ctyunique_ids(self):
        cty1 = City()
        cty2 = City()
        self.assertNotEqual(cty1.id, cty2.id)

    def test_two_created_at(self):
        cty1 = City()
        sleep(0.05)
        cty2 = City()
        self.assertLess(cty1.created_at, cty2.created_at)

    def test_two_cities_different(self):
        cty1 = City()
        sleep(0.05)
        cty2 = City()
        self.assertLess(cty1.updated_at, cty2.updated_at)

    def test_str_representation(self):
        dat = datetime.today()
        dat_repr = repr(dat)
        cty = City()
        cty.id = "123456"
        cty.created_at = cty.updated_at = dat
        cystr = cty.__str__()
        self.assertIn("[City] (123456)", cystr)
        self.assertIn("'id': '123456'", cystr)
        self.assertIn("'created_at': " + dat_repr, cystr)
        self.assertIn("'updated_at': " + dat_repr, cystr)

    def test_args_notused(self):
        cty = City(None)
        self.assertNotIn(None, cty.__dict__.values())

    def test_instant_withkwargs(self):
        dat = datetime.today()
        dat_iso = dat.isoformat()
        cty = City(id="345", created_at=dat_iso, updated_at=dat_iso)
        self.assertEqual(cty.id, "345")
        self.assertEqual(cty.created_at, dat)
        self.assertEqual(cty.updated_at, dat)

    def test_with_out_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


class TestCity_Aregawi(unittest.TestCase):
    """Unittests to test this method class class."""

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
        cty = City()
        sleep(0.05)
        first_updated_at = cty.updated_at
        cty.save()
        self.assertLess(first_updated_at, cty.updated_at)

    def test_twosaves(self):
        cty = City()
        sleep(0.05)
        first_updated_at = cty.updated_at
        cty.save()
        second_updated_at = cty.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        cty.save()
        self.assertLess(second_updated_at, cty.updated_at)

    def test_save_with_argument(self):
        cty = City()
        with self.assertRaises(TypeError):
            cty.save(None)

    def test_save_updates(self):
        cty = City()
        cty.save()
        cyid = "City." + cty.id
        with open("file.json", "r") as f:
            self.assertIn(cyid, f.read())


class TestCity_Teklay(unittest.TestCase):
    """Unittests to test this method class of City."""

    def test_to_dicttype(self):
        self.assertTrue(dict, type(City().to_dict()))

    def test_to_dict_keys(self):
        cty = City()
        self.assertIn("id", cty.to_dict())
        self.assertIn("created_at", cty.to_dict())
        self.assertIn("updated_at", cty.to_dict())
        self.assertIn("__class__", cty.to_dict())

    def test_to_dict_contains(self):
        cty = City()
        cty.middle_name = "Holberton"
        cty.my_number = 98
        self.assertEqual("Holberton", cty.middle_name)
        self.assertIn("my_number", cty.to_dict())

    def test_to_dict_datetime(self):
        cty = City()
        cty_dict = cty.to_dict()
        self.assertEqual(str, type(cty_dict["id"]))
        self.assertEqual(str, type(cty_dict["created_at"]))
        self.assertEqual(str, type(cty_dict["updated_at"]))

    def test_to_dictoutput(self):
        dat = datetime.today()
        cty = City()
        cty.id = "123456"
        cty.created_at = cty.updated_at = dat
        tdict = {
            'id': '123456',
            '__class__': 'City',
            'created_at': dat.isoformat(),
            'updated_at': dat.isoformat(),
        }
        self.assertDictEqual(cty.to_dict(), tdict)

    def test_contrast_to_dict(self):
        cty = City()
        self.assertNotEqual(cty.to_dict(), cty.__dict__)

    def test_to_dict_with_argument(self):
        cty = City()
        with self.assertRaises(TypeError):
            cty.to_dict(None)


if __name__ == "__main__":
    unittest.main()
