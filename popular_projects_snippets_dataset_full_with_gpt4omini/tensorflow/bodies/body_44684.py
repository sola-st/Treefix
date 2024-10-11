# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
self.assertListEqual(list(py_builtins.range_(3)), [0, 1, 2])
self.assertListEqual(list(py_builtins.range_(1, 3)), [1, 2])
self.assertListEqual(list(py_builtins.range_(2, 0, -1)), [2, 1])
