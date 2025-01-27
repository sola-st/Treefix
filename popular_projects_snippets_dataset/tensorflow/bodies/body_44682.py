# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
self.assertEqual(py_builtins.min_([2, 1, 3]), 1)
self.assertEqual(py_builtins.min_(2, 0, 1), 0)
