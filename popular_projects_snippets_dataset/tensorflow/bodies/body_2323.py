# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/conv2d_test.py
expected_output = [20, 30, 20]
self._VerifyValues(
    input_sizes=[1, 1, 4, 1],
    filter_sizes=[1, 3, 1, 1],
    out_backprop_sizes=[1, 1, 4, 1],
    strides=[1, 1],
    padding="SAME",
    data_format_src="NHWC",
    data_format_dst=data_format,
    expected=expected_output)
