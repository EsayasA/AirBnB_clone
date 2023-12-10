#!/usr/bin/python3
"""This is unittests for models/review.py.

Unittest classes:
    TestReview_Esayas
    TestReview_Aregawi
    TestReview_Teklay
"""
import unittest
import models
import os
from datetime import datetime
from time import sleep
from models.review import Review


class TestReview_Esayas(unittest.TestCase):
    """Unittests to test Review class."""

    def test_no_argument(self):
        self.assertEqual(Review, type(Review()))

    def test_stored_in_objects(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_public_str(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at_time(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_time(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_place__class_attribute(self):
        rev = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(rev))
        self.assertNotIn("place_id", rev.__dict__)

    def test_user_id_attribute(self):
        rev = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(rev))
        self.assertNotIn("user_id", rev.__dict__)

    def test_text_is_attribute(self):
        rev = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(rev))
        self.assertNotIn("text", rev.__dict__)

    def test_two_reviews(self):
        rev1 = Review()
        rev2 = Review()
        self.assertNotEqual(rev1.id, rev2.id)

    def test_two_rev_created_at(self):
        rev1 = Review()
        sleep(0.05)
        rev2 = Review()
        self.assertLess(rev1.created_at, rev2.created_at)

    def test_two_rev_updated_at(self):
        rev1 = Review()
        sleep(0.05)
        rev2 = Review()
        self.assertLess(rev1.updated_at, rev2.updated_at)

    def test_str_rep(self):
        dat = datetime.today()
        dat_repr = repr(dat)
        rev = Review()
        rev.id = "123456"
        rev.created_at = rev.updated_at = dat
        rvstr = rev.__str__()
        self.assertIn("[Review] (123456)", rvstr)
        self.assertIn("'id': '123456'", rvstr)
        self.assertIn("'created_at': " + dat_repr, rvstr)
        self.assertIn("'updated_at': " + dat_repr, rvstr)

    def test_args_notused(self):
        rev = Review(None)
        self.assertNotIn(None, rev.__dict__.values())

    def test_instant_wkwargs(self):
        dat = datetime.today()
        dat_iso = dat.isoformat()
        rev = Review(id="345", created_at=dat_iso, updated_at=dat_iso)
        self.assertEqual(rev.id, "345")
        self.assertEqual(rev.created_at, dat)
        self.assertEqual(rev.updated_at, dat)

    def test_instant_with_out_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)


class TestReview_Aregawi(unittest.TestCase):
    """Unittests to test Review class."""

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
        rev = Review()
        sleep(0.05)
        first_updated_at = rev.updated_at
        rev.save()
        self.assertLess(first_updated_at, rev.updated_at)

    def test_twosaves(self):
        rev = Review()
        sleep(0.05)
        first_updated_at = rev.updated_at
        rev.save()
        second_updated_at = rev.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        rev.save()
        self.assertLess(second_updated_at, rev.updated_at)

    def test_save_witharg(self):
        rev = Review()
        with self.assertRaises(TypeError):
            rev.save(None)

    def test_updates_file(self):
        rev = Review()
        rev.save()
        rvid = "Review." + rev.id
        with open("file.json", "r") as f:
            self.assertIn(rvid, f.read())


class TestReview_Teklay(unittest.TestCase):
    """Unittests to test Review class."""

    def test_to_dictype(self):
        self.assertTrue(dict, type(Review().to_dict()))

    def test_dict_correct_keys(self):
        rev = Review()
        self.assertIn("id", rev.to_dict())
        self.assertIn("created_at", rev.to_dict())
        self.assertIn("updated_at", rev.to_dict())
        self.assertIn("__class__", rev.to_dict())

    def test_to_dict_contains(self):
        rev = Review()
        rev.middle_name = "Holberton"
        rev.my_number = 98
        self.assertEqual("Holberton", rev.middle_name)
        self.assertIn("my_number", rev.to_dict())

    def test_datetime_attributes_are_strs(self):
        rev = Review()
        rev_dict = rev.to_dict()
        self.assertEqual(str, type(rev_dict["id"]))
        self.assertEqual(str, type(rev_dict["created_at"]))
        self.assertEqual(str, type(rev_dict["updated_at"]))

    def test_dic_output(self):
        dat = datetime.today()
        rev = Review()
        rev.id = "123456"
        rev.created_at = rev.updated_at = dat
        tdict = {
            'id': '123456',
            '__class__': 'Review',
            'created_at': dat.isoformat(),
            'updated_at': dat.isoformat(),
        }
        self.assertDictEqual(rev.to_dict(), tdict)

    def test_contrast_to_dict(self):
        rev = Review()
        self.assertNotEqual(rev.to_dict(), rev.__dict__)

    def test_with_argument(self):
        rev = Review()
        with self.assertRaises(TypeError):
            rev.to_dict(None)


if __name__ == "__main__":
    unittest.main()
