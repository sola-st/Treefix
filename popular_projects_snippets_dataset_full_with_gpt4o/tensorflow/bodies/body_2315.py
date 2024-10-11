# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/conv2d_test.py
expected_output = [8056, 8432, 8312, 8704, 8568, 8976]
self._VerifyValues(
    input_sizes=[1, 4, 4, 3],
    filter_sizes=[1, 1, 3, 2],
    out_backprop_sizes=[1, 4, 4, 2],
    strides=[1, 1],
    padding="VALID",
    data_format_src="NHWC",
    data_format_dst=data_format,
    expected=expected_output)
