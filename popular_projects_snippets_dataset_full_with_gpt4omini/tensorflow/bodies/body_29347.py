# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/sparse_test.py
classes = classes_fn()
expected = expected_fn()
self.assertEqual(sparse.get_classes(classes), expected)
