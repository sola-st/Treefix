# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/data_structures_test.py
l = []
self.assertAllEqual(data_structures.list_append(l, 1), [1])
self.assertAllEqual(data_structures.list_append(l, 2), [1, 2])
