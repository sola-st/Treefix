# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py
x = constant_op.constant("x", dtype=dtypes.string)

with self.assertRaisesRegex(ValueError, "callable"):
    _ = script_ops.eager_py_func(x, inp=[x], Tout=dtypes.string)
