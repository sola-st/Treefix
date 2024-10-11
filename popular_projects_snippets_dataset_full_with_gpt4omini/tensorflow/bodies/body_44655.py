# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/data_structures_test.py
l = [1, 2, 3]
opts = data_structures.ListPopOpts(element_dtype=None, element_shape=())
self.assertAllEqual(data_structures.list_pop(l, None, opts), ([1, 2], 3))
self.assertAllEqual(data_structures.list_pop(l, None, opts), ([1], 2))
