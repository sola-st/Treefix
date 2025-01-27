# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
"""Verifies the output values of the separable convolution function.

    Args:
      tensor_in_sizes: Input tensor dimensions.
      depthwise_filter_in_sizes: Depthwise filter tensor dimensions.
      pointwise_filter_in_sizes: Pointwise filter tensor dimensions.
      stride: Stride.
      padding: Padding type.
      expected: An array containing the expected operation outputs.
      data_format: string data format for input tensor.
    """
with self.cached_session():
    t1 = self._InitValues(tensor_in_sizes)
    f1 = self._InitValues(depthwise_filter_in_sizes)
    f1.set_shape(depthwise_filter_in_sizes)
    f2 = self._InitValues(pointwise_filter_in_sizes)

    real_t1 = t1
    strides = [1, stride, stride, 1]
    if data_format == "NCHW":
        real_t1 = array_ops.transpose(t1, [0, 3, 1, 2])
        strides = [1, 1, stride, stride]
        if isinstance(padding, list):
            padding = [padding[0], padding[3], padding[1], padding[2]]

    conv = nn_impl.separable_conv2d(
        real_t1,
        f1,
        f2,
        strides=strides,
        padding=padding,
        data_format=data_format)

    if data_format == "NCHW":
        conv = array_ops.transpose(conv, [0, 2, 3, 1])

    value = self.evaluate(conv)
tf_logging.debug("value = %s", value)
self.assertArrayNear(expected, np.ravel(value), 2e-3)
self.assertShapeEqual(value, conv)
