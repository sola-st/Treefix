# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_test.py
with self.assertRaises(ValueError):
    array_ops.placeholder(dtypes_lib.float32, shape=(-1, 10))
