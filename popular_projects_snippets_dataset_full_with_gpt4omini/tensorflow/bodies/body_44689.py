# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
self.assertListEqual(
    list(py_builtins.zip_([3, 2, 1], [1, 2, 3])), [(3, 1), (2, 2), (1, 3)])
self.assertListEqual(
    list(py_builtins.zip_([4, 5, 6], [-1, -2])), [(4, -1), (5, -2)])
