# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
root = autotrackable.AutoTrackable()
orig_dict = {"a": [1.]}
root.a = orig_dict
copied = copy.copy(root.a)
self.assertAllEqual([1.], copied["a"])
self.assertIsNot(root.a, copied)
self.assertIs(root.a["a"], copied["a"])

copied = root.a.copy()
self.assertAllEqual([1.], copied["a"])
self.assertIsNot(root.a, copied)
self.assertIs(root.a["a"], copied["a"])

# Dirtiness should be inherited
util.list_objects(root.a)
orig_dict["b"] = []
with self.assertRaises(ValueError):
    util.list_objects(root.a)
with self.assertRaises(ValueError):
    util.list_objects(copy.copy(root.a))
