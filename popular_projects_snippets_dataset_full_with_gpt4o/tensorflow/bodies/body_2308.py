# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/conv2d_test.py
self._VerifyValues(
    input_sizes=[1, 3, 6, 1],
    filter_sizes=[2, 2, 1, 1],
    out_backprop_sizes=[1, 1, 5, 1],
    strides=[1, 1],
    dilations=[2, 1],
    padding="VALID",
    data_format_src="NHWC",
    data_format_dst=data_format,
    expected=[1, 4, 7, 10, 13, 10, 0, 0, 0, 0, 0, 0, 3, 10, 17, 24, 31, 20])
