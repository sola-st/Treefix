# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
tensor_in_sizes = [1, 4, 4, 2]
depthwise_filter_in_sizes = [2, 2, 2, 3]
pointwise_filter_in_sizes = [1, 1, 6, 7]
padding = [[0, 0], [1, 2], [3, 4], [0, 0]]
with self.cached_session():
    # Compute the 'expected' values by manually padding before calling
    # separable_conv2d
    t1 = self._InitValues(tensor_in_sizes)
    t1 = array_ops.pad(t1, padding)
    f1 = self._InitValues(depthwise_filter_in_sizes)
    f1.set_shape(depthwise_filter_in_sizes)
    f2 = self._InitValues(pointwise_filter_in_sizes)
    conv = nn_impl.separable_conv2d(
        t1,
        f1,
        f2,
        strides=[1, 1, 1, 1],
        padding="VALID",
        data_format="NHWC")
    expected = self.evaluate(conv)
    expected = np.ravel(expected)
self._VerifyValues(
    tensor_in_sizes=tensor_in_sizes,
    depthwise_filter_in_sizes=depthwise_filter_in_sizes,
    pointwise_filter_in_sizes=pointwise_filter_in_sizes,
    stride=1,
    padding=padding,
    expected=expected,
    data_format=data_format)
