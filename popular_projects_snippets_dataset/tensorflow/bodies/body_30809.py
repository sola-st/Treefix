# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv3d_backprop_filter_v2_grad_test.py
strides = [1, 1, 1, 1, 1]
padding = "VALID"
tin = constant_op.constant(
    .5053710941, shape=[2, 2, 2, 2, 1], dtype=dtypes.float32)
filter_sizes = constant_op.constant(0, shape=[], dtype=dtypes.int32)
out_backprop = constant_op.constant(
    .5053710941, shape=[2, 2, 2, 2, 1], dtype=dtypes.float32)

with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            "must be rank 1"):
    nn_ops.conv3d_backprop_filter_v2(
        input=tin,
        filter_sizes=filter_sizes,
        out_backprop=out_backprop,
        strides=strides,
        padding=padding)
