# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
l = data_structures.ListWrapper([1, 2, 3, [4]])
del l[2:3]
self.assertEqual(l, [1, 2, [4]])
self.assertUnableToSave(l, "Unable to save .*__delslice__")
