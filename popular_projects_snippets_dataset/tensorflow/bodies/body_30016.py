# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_eager_test.py
# Non-vector dimensions.
with self.assertRaises(errors_impl.InvalidArgumentError):
    array_ops.fill([[0, 1], [2, 3]], 1.0)

# Non-scalar value.
with self.assertRaises(errors_impl.InvalidArgumentError):
    array_ops.fill([3, 2], [1.0, 2.0])
