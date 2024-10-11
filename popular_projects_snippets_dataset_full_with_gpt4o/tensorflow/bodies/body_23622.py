# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
l = data_structures.ListWrapper([1, 2, 3, [4]])
l *= -1
self.assertEqual(l, [1, 2, 3, [4]] * -1)
self.assertUnableToSave(l, "Unable to save")
