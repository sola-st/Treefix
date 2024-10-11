# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/conv2d_test.py
self._VerifyValues(
    input_sizes=[1, 3, 3, 1],
    filter_sizes=[2, 2, 1, 2],
    out_backprop_sizes=[1, 1, 1, 2],
    strides=[1, 1],
    dilations=[2, 2],
    padding="VALID",
    data_format_src="NHWC",
    data_format_dst=data_format,
    expected=[5, 0, 11, 0, 0, 0, 17, 0, 23])
