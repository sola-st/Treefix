# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/conv2d_test.py
expected_output = [5, 8, 14, 17]
self._VerifyValues(
    input_sizes=[1, 2, 3, 1],
    filter_sizes=[2, 2, 1, 1],
    out_backprop_sizes=[1, 1, 2, 1],
    strides=[1, 1],
    padding="VALID",
    data_format_src="NHWC",
    data_format_dst=data_format,
    expected=expected_output)
