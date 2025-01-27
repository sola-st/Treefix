# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
self.assertListEqual(
    list(py_builtins.filter_(lambda x: x == 'b', ['a', 'b', 'c'])), ['b'])
self.assertListEqual(
    list(py_builtins.filter_(lambda x: x < 3, [3, 2, 1])), [2, 1])
