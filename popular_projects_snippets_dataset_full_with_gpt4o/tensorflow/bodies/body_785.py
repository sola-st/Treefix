# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/depthwise_conv_op_test.py
"""Verifies the output values of the depthwise convolution function.

    Args:
      tensor_in_sizes: Input tensor dimensions in
        [batch, input_rows, input_cols, input_depth].
      filter_in_sizes: Filter tensor dimensions in
        [filter_rows, filter_cols, input_depth, depth_multiplier].
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
x1 = np.array([f * 1.0 for f in range(1, total_size_1 + 1)],
              dtype=np.float32).reshape(tensor_in_sizes)
x2 = np.array([f * 1.0 for f in range(1, total_size_2 + 1)],
              dtype=np.float32).reshape(filter_in_sizes)
with self.session() as sess:
    t1 = array_ops.placeholder(shape=tensor_in_sizes, dtype=np.float32)
    t2 = array_ops.placeholder(shape=filter_in_sizes, dtype=np.float32)
    with self.test_scope():
        conv = nn_ops.depthwise_conv2d_native(
            t1, t2, strides=[1, stride, stride, 1], padding=padding)
    value = sess.run(conv, {t1: x1, t2: x2})
print("value = ", value)
self.assertArrayNear(expected, np.ravel(value), 1e-4)
self.assertShapeEqual(value, conv)
