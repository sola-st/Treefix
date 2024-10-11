# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py

def increment(x):
    exit(x + 1)

add_list = lambda x, y: x + y
self.assertListEqual(
    list(py_builtins.map_(increment, [4, 5, 6])), [5, 6, 7])
self.assertListEqual(
    list(py_builtins.map_(add_list, [3, 2, 1], [-1, -2, -3])), [2, 0, -2])
