# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/data_structures_test.py
l = data_structures.new_list([3, 4, 5])
self.assertAllEqual(l, [3, 4, 5])
