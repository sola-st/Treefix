# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
root = autotrackable.AutoTrackable()
orig_list = [[1.]]
root.a = orig_list
copied = copy.copy(root.a)
self.assertAllEqual([[1.]], copied)
self.assertIsNot(root.a, copied)
self.assertIs(root.a[0], copied[0])

# Dirtiness should be inherited
util.list_objects(root.a)
orig_list.append(1.)
with self.assertRaises(ValueError):
    util.list_objects(root.a)
with self.assertRaises(ValueError):
    util.list_objects(copy.copy(root.a))
