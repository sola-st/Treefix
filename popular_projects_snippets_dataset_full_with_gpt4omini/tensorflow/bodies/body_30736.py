# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/concat_op_test.py
# Rank doesn't match.
with self.assertRaises(ValueError):
    array_ops.concat(
        [constant_op.constant(10.0, shape=[4, 4, 4, 4]),
         constant_op.constant(20.0, shape=[4, 4, 4])
        ], 1)

# Dimensions don't match in a non-concat dim.
with self.assertRaises(ValueError):
    array_ops.concat(
        [constant_op.constant(10.0, shape=[1, 2, 1]),
         constant_op.constant(20.0, shape=[3, 2, 1])
        ], 1)

# concat_dim out of range.
with self.assertRaises(ValueError):
    array_ops.concat(
        [constant_op.constant(10.0, shape=[4, 4, 4]),
         constant_op.constant(20.0, shape=[4, 4, 4])
        ], 3)

# concat_dim out of range
with self.assertRaises(ValueError):
    array_ops.concat(
        [constant_op.constant(10.0, shape=[4, 4, 4]),
         constant_op.constant(20.0, shape=[4, 4, 4])
        ], -4)
