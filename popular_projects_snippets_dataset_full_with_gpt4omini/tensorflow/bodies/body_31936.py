# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv1d_test.py
"""Test that argument passing to conv1d is handled properly."""
# double datatype is currently not supported for convolution ops
# on the ROCm platform
x = constant_op.constant([1, 2, 3, 4], dtype=dtypes.float32)
x = array_ops.expand_dims(x, 0)  # Add batch dimension
x = array_ops.expand_dims(x, 2)  # And depth dimension
x = array_ops.stack([x, x])  # Make batch shape [2, 1]
filters = constant_op.constant([2, 1], dtype=dtypes.float32)
filters = array_ops.expand_dims(filters, 1)  # in_channels
filters = array_ops.expand_dims(filters, 2)  # out_channels
# Filters is 2x1x1
for stride in [1, 2]:
    with self.cached_session(use_gpu=test.is_gpu_available()):
        c = nn_ops.conv1d(x, filters, stride, padding="VALID")
        reduced = array_ops.squeeze(c)  # Sequeeze out dims 1 and 3.
        output = self.evaluate(reduced)
        if stride == 1:
            self.assertAllClose(output,
                                [[2 * 1 + 1 * 2, 2 * 2 + 1 * 3, 2 * 3 + 1 * 4],
                                 [2 * 1 + 1 * 2, 2 * 2 + 1 * 3, 2 * 3 + 1 * 4]])
        else:
            self.assertAllClose(
                output,
                [[2 * 1 + 1 * 2, 2 * 3 + 1 * 4], [2 * 1 + 1 * 2, 2 * 3 + 1 * 4]])
