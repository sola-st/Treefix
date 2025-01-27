# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/conv2d_test.py
expected_output = [92, 102, 112]
self._VerifyValues(
    input_sizes=[1, 3, 5, 1],
    filter_sizes=[1, 3, 1, 1],
    out_backprop_sizes=[1, 2, 2, 1],
    strides=[2, 2],
    padding="VALID",
    data_format_src="NHWC",
    data_format_dst=data_format,
    expected=expected_output)
