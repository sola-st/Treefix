# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_test.py
# Test case for GitHub issue 18474
with self.assertRaises(TypeError):
    constant_op.constant(dtypes_lib.string, "[,]")
