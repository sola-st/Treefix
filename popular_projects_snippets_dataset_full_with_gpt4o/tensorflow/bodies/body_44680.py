# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
self.assertEqual(py_builtins.max_([1, 3, 2]), 3)
self.assertEqual(py_builtins.max_(0, 2, 1), 2)
