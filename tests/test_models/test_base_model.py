#!/usr/bin/python3
"""This ex[laons to unittests for models/base_model.py.

Unittest classes:
    TestBaseModel_Esayas
    TestBaseModel_Aregawi
    TestBaseModel_Teklay
"""
import models
import unittest
import os
from time import sleep
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel_Esayas(unittest.TestCase):
    """Unittests to test instantiation of the BaseModel class."""

    def test_without_argument_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_stored_in_object(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_idpublic_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_attime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_models_uniqueids(self):
        mb1 = BaseModel()
        mb2 = BaseModel()
        self.assertNotEqual(mb1.id, mb2.id)

    def test_two_models_created_at(self):
        mb1 = BaseModel()
        sleep(0.05)
        mb2 = BaseModel()
        self.assertLess(mb1.created_at, mb2.created_at)

    def test_two_models__updated_at(self):
        mb1 = BaseModel()
        sleep(0.05)
        mb2 = BaseModel()
        self.assertLess(mb1.updated_at, mb2.updated_at)

    def test_str_representat(self):
        dat = datetime.today()
        dat_repr = repr(dat)
        mb = BaseModel()
        mb.id = "123456"
        mb.created_at = mb.updated_at = dat
        bmstr = mb.__str__()
        self.assertIn("[BaseModel] (123456)", bmstr)
        self.assertIn("'id': '123456'", bmstr)
        self.assertIn("'created_at': " + dat_repr, bmstr)
        self.assertIn("'updated_at': " + dat_repr, bmstr)

    def test_args_notused(self):
        mb = BaseModel(None)
        self.assertNotIn(None, mb.__dict__.values())

    def test_instant_with_kwargs(self):
        dat = datetime.today()
        dat_iso = dat.isoformat()
        mb = BaseModel(id="345", created_at=dat_iso, updated_at=dat_iso)
        self.assertEqual(mb.id, "345")
        self.assertEqual(mb.created_at, dat)
        self.assertEqual(mb.updated_at, dat)

    def test_instantiation_withempty_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_withargu_and_kwargs(self):
        dat = datetime.today()
        dat_iso = dat.isoformat()
        mb = BaseModel("12", id="345", created_at=dat_iso, updated_at=dat_iso)
        self.assertEqual(mb.id, "345")
        self.assertEqual(mb.created_at, dat)
        self.assertEqual(mb.updated_at, dat)


class TestBaseModel_Aregawi(unittest.TestCase):
    """Unittests to test aregawi method of the BaseModel class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_forsave(self):
        mb = BaseModel()
        sleep(0.05)
        first_updated_at = mb.updated_at
        mb.save()
        self.assertLess(first_updated_at, mb.updated_at)

    def test_twosaves(self):
        mb = BaseModel()
        sleep(0.05)
        first_updated_at = mb.updated_at
        mb.save()
        second_updated_at = mb.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        mb.save()
        self.assertLess(second_updated_at, mb.updated_at)

    def test_save_argu(self):
        mb = BaseModel()
        with self.assertRaises(TypeError):
            mb.save(None)

    def test_save_updates(self):
        mb = BaseModel()
        mb.save()
        bmid = "BaseModel." + mb.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())


class TestBaseModel_Teklay(unittest.TestCase):
    """Unittests to testi teklay of BaseModel class."""

    def test_to_dicttype(self):
        mb = BaseModel()
        self.assertTrue(dict, type(mb.to_dict()))

    def test_to_dict_keys(self):
        mb = BaseModel()
        self.assertIn("id", mb.to_dict())
        self.assertIn("created_at", mb.to_dict())
        self.assertIn("updated_at", mb.to_dict())
        self.assertIn("__class__", mb.to_dict())

    def test_to_dict_attributes(self):
        mb = BaseModel()
        mb.name = "Holberton"
        mb.my_number = 98
        self.assertIn("name", mb.to_dict())
        self.assertIn("my_number", mb.to_dict())

    def test_to_dict_datestrs(self):
        mb = BaseModel()
        mb_dict = mb.to_dict()
        self.assertEqual(str, type(mb_dict["created_at"]))
        self.assertEqual(str, type(mb_dict["updated_at"]))

    def test_to_dicoutput(self):
        dat = datetime.today()
        mb = BaseModel()
        mb.id = "123456"
        mb.created_at = mb.updated_at = dat
        tdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dat.isoformat(),
            'updated_at': dat.isoformat()
        }
        self.assertDictEqual(mb.to_dict(), tdict)

    def test_contrast_to_dict(self):
        mb = BaseModel()
        self.assertNotEqual(mb.to_dict(), mb.__dict__)

    def test_to_dict_argument(self):
        mb = BaseModel()
        with self.assertRaises(TypeError):
            mb.to_dict(None)


if __name__ == "__main__":
    unittest.main()
