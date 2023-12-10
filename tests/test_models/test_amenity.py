#!/usr/bin/python3
"""This explaines for  unittests to models/amenity.py.

Unittest classes:
    TestAmenity_Esayas
    TestAmenity_Aregawi
    TestAmenity_Teklay
"""
import models
import os
import unittest
from time import sleep
from datetime import datetime
from models.amenity import Amenity


class TestAmenity_Esayas(unittest.TestCase):
    """Unittests to test class of instant."""

    def test_with_out_argument(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_stored_at_object(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_public_id_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_time(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_time(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_public_name(self):
        me = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", me.__dict__)

    def test_idt_amenities(self):
        me1 = Amenity()
        me2 = Amenity()
        self.assertNotEqual(me1.id, me2.id)

    def test_amenities_created_at(self):
        me1 = Amenity()
        sleep(0.05)
        me2 = Amenity()
        self.assertLess(me1.created_at, me2.created_at)

    def test_amenities_updated_at(self):
        me1 = Amenity()
        sleep(0.05)
        me2 = Amenity()
        self.assertLess(me1.updated_at, me2.updated_at)

    def test_str_repres(self):
        dat = datetime.today()
        dat_repr = repr(dat)
        me = Amenity()
        me.id = "123456"
        me.created_at = me.updated_at = dat
        amstr = me.__str__()
        self.assertIn("[Amenity] (123456)", amstr)
        self.assertIn("'id': '123456'", amstr)
        self.assertIn("'created_at': " + dat_repr, amstr)
        self.assertIn("'updated_at': " + dat_repr, amstr)

    def test_argument(self):
        me = Amenity(None)
        self.assertNotIn(None, me.__dict__.values())

    def test_with_kwargs(self):
        """instant for kwargs test method"""
        dat = datetime.today()
        dat_iso = dat.isoformat()
        me = Amenity(id="345", created_at=dat_iso, updated_at=dat_iso)
        self.assertEqual(me.id, "345")
        self.assertEqual(me.created_at, dat)
        self.assertEqual(me.updated_at, dat)

    def test__empty_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class TestAmenity_Aregawi(unittest.TestCase):
    """Unittests to test method of the class."""

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

    def test_for_save(self):
        me = Amenity()
        sleep(0.05)
        first_updated_at = me.updated_at
        me.save()
        self.assertLess(first_updated_at, me.updated_at)

    def test_sec_saves(self):
        me = Amenity()
        sleep(0.05)
        first_updated_at = me.updated_at
        me.save()
        second_updated_at = me.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        me.save()
        self.assertLess(second_updated_at, me.updated_at)

    def test_save_with_argument(self):
        me = Amenity()
        with self.assertRaises(TypeError):
            me.save(None)

    def test_save_withs_update_file(self):
        me = Amenity()
        me.save()
        amid = "Amenity." + me.id
        with open("file.json", "r") as f:
            self.assertIn(amid, f.read())


class TestAmenity_Teklay(unittest.TestCase):
    """Unittests for to tests the teklay method."""

    def test_dict_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_tocontains_correct_keys(self):
        me = Amenity()
        self.assertIn("id", me.to_dict())
        self.assertIn("created_at", me.to_dict())
        self.assertIn("updated_at", me.to_dict())
        self.assertIn("__class__", me.to_dict())

    def test_to_added_attributes(self):
        me = Amenity()
        me.middle_name = "Holberton"
        me.my_number = 98
        self.assertEqual("Holberton", me.middle_name)
        self.assertIn("my_number", me.to_dict())

    def test_to_attributes_are_strs(self):
        me = Amenity()
        me_dict = me.to_dict()
        self.assertEqual(str, type(me_dict["id"]))
        self.assertEqual(str, type(me_dict["created_at"]))
        self.assertEqual(str, type(me_dict["updated_at"]))

    def test_todict_output(self):
        dat = datetime.today()
        me = Amenity()
        me.id = "123456"
        me.created_at = me.updated_at = dat
        tdict = {
            'id': '123456',
            '__class__': 'Amenity',
            'created_at': dat.isoformat(),
            'updated_at': dat.isoformat(),
        }
        self.assertDictEqual(me.to_dict(), tdict)

    def test_contrast_with_dict_dunder_dict(self):
        me = Amenity()
        self.assertNotEqual(me.to_dict(), me.__dict__)

    def test_towith_arg(self):
        me = Amenity()
        with self.assertRaises(TypeError):
            me.to_dict(None)


if __name__ == "__main__":
    unittest.main()
