# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/conv2d_test.py
expected_output = [1, 4, 3, 8, 5, 12, 7, 16]
self._VerifyValues(
    input_sizes=[1, 2, 2, 2],
    filter_sizes=[2, 2, 1, 2],
    out_backprop_sizes=[1, 1, 1, 2],
    strides=[1, 1],
    padding="VALID",
    data_format_src="NHWC",
    data_format_dst=data_format,
    expected=expected_output)
