# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
with self.assertRaises(ValueError):
    py_builtins.len_(constant_op.constant(1))
