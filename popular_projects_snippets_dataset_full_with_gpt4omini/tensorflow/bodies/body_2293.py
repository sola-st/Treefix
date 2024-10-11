# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/conv2d_test.py
self._VerifyValues(
    input_sizes=[1, 2, 3, 3],
    filter_sizes=[2, 2, 3, 3],
    strides=[1, 1],
    dilations=[1, 2],
    padding="VALID",
    data_format_src="NHWC",
    data_format_dst=data_format,
    expected=np.reshape([2667, 2781, 2895], [1, 1, 1, 3]))
