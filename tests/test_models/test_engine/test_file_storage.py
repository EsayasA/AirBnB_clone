#!/usr/bin/python3
"""This explains unittest for models/engine/file_storage.py.

Unittest classes:
    TestFileStorage_Esayas
    TestFileStorage_Aregawi
"""
import json
import models
import os
import unittest
from models.city import City
from models.state import State
from models.place import Place
from models.user import User
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models.review import Review


class TestFileStorage_Esayas(unittest.TestCase):
    """Unittest to test FileStorage class."""

    def test_FileStorage_empty_argument(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_with_argument(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_isprivate(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_isprivate_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_init(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_Aregawi(unittest.TestCase):
    """Unittest to test FileStorage class."""

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
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_with_argument(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_newfrom(self):
        mb = BaseModel()
        use = User()
        sta = State()
        pla = Place()
        cty = City()
        me = Amenity()
        rev = Review()
        models.storage.new(mb)
        models.storage.new(use)
        models.storage.new(sta)
        models.storage.new(pla)
        models.storage.new(cty)
        models.storage.new(me)
        models.storage.new(rev)
        self.assertIn("BaseModel." + mb.id, models.storage.all().keys())
        self.assertIn(mb, models.storage.all().values())
        self.assertIn("User." + use.id, models.storage.all().keys())
        self.assertIn(use, models.storage.all().values())
        self.assertIn("State." + sta.id, models.storage.all().keys())
        self.assertIn(sta, models.storage.all().values())
        self.assertIn("Place." + pla.id, models.storage.all().keys())
        self.assertIn(pla, models.storage.all().values())
        self.assertIn("City." + cty.id, models.storage.all().keys())
        self.assertIn(cty, models.storage.all().values())
        self.assertIn("Amenity." + me.id, models.storage.all().keys())
        self.assertIn(me, models.storage.all().values())
        self.assertIn("Review." + rev.id, models.storage.all().keys())
        self.assertIn(rev, models.storage.all().values())

    def test_with_argument(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_save(self):
        mb = BaseModel()
        use = User()
        sta = State()
        pla = Place()
        cty = City()
        me = Amenity()
        rev = Review()
        models.storage.new(mb)
        models.storage.new(use)
        models.storage.new(sta)
        models.storage.new(pla)
        models.storage.new(cty)
        models.storage.new(me)
        models.storage.new(rev)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + mb.id, save_text)
            self.assertIn("User." + use.id, save_text)
            self.assertIn("State." + sta.id, save_text)
            self.assertIn("Place." + pla.id, save_text)
            self.assertIn("City." + cty.id, save_text)
            self.assertIn("Amenity." + me.id, save_text)
            self.assertIn("Review." + rev.id, save_text)

    def test_with_argument(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        mb = BaseModel()
        use = User()
        sta = State()
        pla = Place()
        cty = City()
        me = Amenity()
        rev = Review()
        models.storage.new(mb)
        models.storage.new(use)
        models.storage.new(sta)
        models.storage.new(pla)
        models.storage.new(cty)
        models.storage.new(me)
        models.storage.new(rev)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + mb.id, objs)
        self.assertIn("User." + use.id, objs)
        self.assertIn("State." + sta.id, objs)
        self.assertIn("Place." + pla.id, objs)
        self.assertIn("City." + cty.id, objs)
        self.assertIn("Amenity." + me.id, objs)
        self.assertIn("Review." + rev.id, objs)

    def test_reload_with_argument(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
