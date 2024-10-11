# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/quantized_conv_ops_test.py
"""Verifies the output values of the convolution function.

    Args:
      tensor_in_sizes: Input tensor dimensions in
        [batch, input_rows, input_cols, input_depth].
      filter_in_sizes: Filter tensor dimensions in
        [kernel_rows, kernel_cols, input_depth, output_depth].
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
x1 = np.array([f for f in range(1, total_size_1 + 1)])
x1 = x1.astype(np.uint8).reshape(tensor_in_sizes)
x1_min = 0.0
x1_max = 255.0
x2 = np.array([f for f in range(1, total_size_2 + 1)]).astype(np.uint8)
x2 = x2.astype(np.uint8).reshape(filter_in_sizes)
x2_min = 0.0
x2_max = 255.0
with self.cached_session(use_gpu=False) as sess:
    t1 = constant_op.constant(x1, shape=tensor_in_sizes, dtype=dtypes.quint8)
    t2 = constant_op.constant(x2, shape=filter_in_sizes, dtype=dtypes.quint8)
    conv = nn_ops.quantized_conv2d(
        t1,
        t2,
        out_type=dtypes.qint32,
        strides=[1, stride, stride, 1],
        padding=padding,
        min_input=x1_min,
        max_input=x1_max,
        min_filter=x2_min,
        max_filter=x2_max)
    value = self.evaluate(conv)
quantized_output = value[0]
output_min = value[1]
output_max = value[2]
float_output = self._QuantizedOutputToFloat(quantized_output, output_min,
                                            output_max)
self.assertArrayNear(expected, float_output.flatten(), 1.0)
self.assertEqual(value[0].shape, conv[0].get_shape())
