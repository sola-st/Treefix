# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
self.assertListEqual(py_builtins.sorted_([2, 3, 1]), [1, 2, 3])
self.assertListEqual(
    py_builtins.sorted_([2, 3, 1], key=lambda x: -x), [3, 2, 1])
self.assertListEqual(
    py_builtins.sorted_([2, 3, 1], reverse=True), [3, 2, 1])
self.assertListEqual(
    py_builtins.sorted_([2, 3, 1], key=lambda x: -x, reverse=True),
    [1, 2, 3])
self.assertAllEqual(
    py_builtins.sorted_([[4, 3], [2, 1]], key=lambda x: sum(x)),
    [[2, 1], [4, 3]])
