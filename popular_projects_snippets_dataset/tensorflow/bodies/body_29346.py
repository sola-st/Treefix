# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/sparse_test.py
types = types_fn()
classes = classes_fn()
expected = expected_fn()
self.assertEqual(sparse.as_dense_types(types, classes), expected)
