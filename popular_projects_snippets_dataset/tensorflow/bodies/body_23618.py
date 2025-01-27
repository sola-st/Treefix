# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
l = data_structures.ListWrapper([1, 2, 3, 4])
l[:] = 2, 8, 9, 0
self.assertEqual(l, [2, 8, 9, 0])
l._maybe_initialize_trackable()  # pylint: disable=protected-access
self.assertEqual(len(l._trackable_children()), 0)  # pylint: disable=protected-access
