# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/spacetobatch_op_test.py
tf_in = constant_op.constant(
    -3.5e+35, shape=[10, 19, 22], dtype=dtypes.float32)
block_shape = constant_op.constant(
    1879048192, shape=[2], dtype=dtypes.int64)
paddings = constant_op.constant(0, shape=[2, 2], dtype=dtypes.int32)
with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            "Negative.* dimension size caused by overflow"):
    array_ops.space_to_batch_nd(tf_in, block_shape, paddings)
