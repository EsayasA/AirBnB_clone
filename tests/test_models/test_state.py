#!/usr/bin/python3
"""This explains unittests for models/state.py.

Unittest classes:
    TestState_Esayas
    TestState_Aregawi
    TestState_Teklay
"""
import unittest
import os
import models
from time import sleep
from datetime import datetime
from models.state import State


class TestState_Esayas(unittest.TestCase):
    """Unittests to test State class."""

    def test_no_argument_instant(self):
        self.assertEqual(State, type(State()))

    def test_stored_in_objects(self):
        self.assertIn(State(), models.storage.all().values())

    def test_public_id_str(self):
        self.assertEqual(str, type(State().id))

    def test_created_at_time(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_updated_at_time(self):
        self.assertEqual(datetime, type(State().updated_at))

    def test_public_name_class_attribute(self):
        sta = State()
        self.assertEqual(str, type(State.name))
        self.assertIn("name", dir(sta))
        self.assertNotIn("name", sta.__dict__)

    def test_twostates_uniqu(self):
        sta1 = State()
        sta2 = State()
        self.assertNotEqual(sta1.id, sta2.id)

    def test_two_states_created(self):
        sta1 = State()
        sleep(0.05)
        sta2 = State()
        self.assertLess(sta1.created_at, sta2.created_at)

    def test_two_states_updated(self):
        sta1 = State()
        sleep(0.05)
        sta2 = State()
        self.assertLess(sta1.updated_at, sta2.updated_at)

    def test_str_represe(self):
        dat = datetime.today()
        dat_repr = repr(dat)
        sta = State()
        sta.id = "123456"
        sta.created_at = sta.updated_at = dat
        ststr = sta.__str__()
        self.assertIn("[State] (123456)", ststr)
        self.assertIn("'id': '123456'", ststr)
        self.assertIn("'created_at': " + dat_repr, ststr)
        self.assertIn("'updated_at': " + dat_repr, ststr)

    def test_args_notused(self):
        sta = State(None)
        self.assertNotIn(None, sta.__dict__.values())

    def test_instanta_with_kwargs(self):
        dat = datetime.today()
        dat_iso = dat.isoformat()
        sta = State(id="345", created_at=dat_iso, updated_at=dat_iso)
        self.assertEqual(sta.id, "345")
        self.assertEqual(sta.created_at, dat)
        self.assertEqual(sta.updated_at, dat)

    def test_instant_with_empty_kwargs(self):
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)


class TestState_Aregawi(unittest.TestCase):
    """Unittests to test State class."""

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
        sta = State()
        sleep(0.05)
        first_updated_at = sta.updated_at
        sta.save()
        self.assertLess(first_updated_at, sta.updated_at)

    def test_twosaves(self):
        sta = State()
        sleep(0.05)
        first_updated_at = sta.updated_at
        sta.save()
        second_updated_at = sta.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        sta.save()
        self.assertLess(second_updated_at, sta.updated_at)

    def test_savewith_argument(self):
        sta = State()
        with self.assertRaises(TypeError):
            sta.save(None)

    def test_updates_file(self):
        sta = State()
        sta.save()
        stid = "State." + sta.id
        with open("file.json", "r") as f:
            self.assertIn(stid, f.read())


class TestState_Teklay(unittest.TestCase):
    """Unittests to test State class."""

    def test_to_dictype(self):
        self.assertTrue(dict, type(State().to_dict()))

    def test_contains_correct_keys(self):
        sta = State()
        self.assertIn("id", sta.to_dict())
        self.assertIn("created_at", sta.to_dict())
        self.assertIn("updated_at", sta.to_dict())
        self.assertIn("__class__", sta.to_dict())

    def test_dic_contains_added(self):
        sta = State()
        sta.middle_name = "Holberton"
        sta.my_number = 98
        self.assertEqual("Holberton", sta.middle_name)
        self.assertIn("my_number", sta.to_dict())

    def test_datetime_attributes_are_strs(self):
        sta = State()
        sta_dict = sta.to_dict()
        self.assertEqual(str, type(sta_dict["id"]))
        self.assertEqual(str, type(sta_dict["created_at"]))
        self.assertEqual(str, type(sta_dict["updated_at"]))

    def test_to_dicoutput(self):
        dat = datetime.today()
        sta = State()
        sta.id = "123456"
        sta.created_at = sta.updated_at = dat
        tdict = {
            'id': '123456',
            '__class__': 'State',
            'created_at': dat.isoformat(),
            'updated_at': dat.isoformat(),
        }
        self.assertDictEqual(sta.to_dict(), tdict)

    def test_contra_dunder_dict(self):
        sta = State()
        self.assertNotEqual(sta.to_dict(), sta.__dict__)

    def test_with_argument(self):
        sta = State()
        with self.assertRaises(TypeError):
            sta.to_dict(None)


if __name__ == "__main__":
    unittest.main()
