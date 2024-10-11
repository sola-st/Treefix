# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
self.assertListEqual(
    list(py_builtins.enumerate_([3, 2, 1])), [(0, 3), (1, 2), (2, 1)])
self.assertListEqual(
    list(py_builtins.enumerate_([3, 2, 1], 5)), [(5, 3), (6, 2), (7, 1)])
self.assertListEqual(list(py_builtins.enumerate_([-8], -3)), [(-3, -8)])
