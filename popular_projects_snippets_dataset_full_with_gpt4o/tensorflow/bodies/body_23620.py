# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
l = data_structures.ListWrapper([1, 2, 3, 4])
l[:] = []
self.assertEqual(l, [])
