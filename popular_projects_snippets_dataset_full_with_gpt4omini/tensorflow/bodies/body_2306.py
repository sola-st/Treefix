# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/conv2d_test.py
expected_output = [1, 2, 5, 4, 6, 0, 0, 0, 0, 0, 3, 6, 13, 8, 12]
self._VerifyValues(
    input_sizes=[1, 3, 5, 1],
    filter_sizes=[1, 3, 1, 1],
    out_backprop_sizes=[1, 2, 2, 1],
    strides=[2, 2],
    padding="VALID",
    data_format_src="NHWC",
    data_format_dst=data_format,
    expected=expected_output)
