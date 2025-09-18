import unittest

from act1.attrdict import AttrDict

class TestAttrDict(unittest.TestCase):

    def test_set_dict_get_dict(self):
        obj = AttrDict()
        obj["name"] = "Martin"
        self.assertEqual(obj["name"], "Martin")

    def test_set_dict_get_attr(self):
        obj = AttrDict()
        obj["name"] = "Martin"
        self.assertEqual(obj.name, "Martin")

    def test_set_attr_get_dict(self):
        obj = AttrDict()
        obj.name = "Martin"
        self.assertEqual(obj["name"], "Martin")

    def test_set_attr_get_attr(self):
        obj = AttrDict()
        obj.name = "Martin"
        self.assertEqual(obj.name, "Martin")


if __name__ == "__main__":
    unittest.main()