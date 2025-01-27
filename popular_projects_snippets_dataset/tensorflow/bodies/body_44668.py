# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
t = constant_op.constant(1, dtype=dtypes.float64)
with self.assertRaises(NotImplementedError):
    py_builtins.int_(t, 2)
