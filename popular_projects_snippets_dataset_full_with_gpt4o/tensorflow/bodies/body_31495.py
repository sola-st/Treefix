# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
"""Verifies the output values of the convolution function.

    Args:
      tensor_in_sizes: Input tensor dimensions in [batch, input_rows,
        input_cols, input_depth].
      filter_in_sizes: Filter tensor dimensions in [filter_rows, filter_cols,
        input_depth, depth_multiplier].
      stride: Stride.
      padding: Padding type.
      expected: An array containing the expected operation outputs.
    """
total_size_1 = 1
total_size_2 = 1
for s in tensor_in_sizes:
    total_size_1 *= s
for s in filter_in_sizes:
    total_size_2 *= s
# Initializes the input tensor with array containing incrementing
# numbers from 1.
x1 = [f * 1.0 for f in range(1, total_size_1 + 1)]
x2 = [f * 1.0 for f in range(1, total_size_2 + 1)]
with self.cached_session():
    t1 = constant_op.constant(x1, shape=tensor_in_sizes)
    t1.set_shape(tensor_in_sizes)
    t2 = constant_op.constant(x2, shape=filter_in_sizes)
    conv = nn_impl.depthwise_conv2d(
        t1, t2, strides=[1, stride, stride, 1], padding=padding)
    value = self.evaluate(conv)
tf_logging.debug("value = %s", value)
self.assertArrayNear(expected, np.ravel(value), 1e-5)
self.assertShapeEqual(value, conv)
