# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/conv2d_test.py
expected_output = [
    5, 11, 17, 11, 25, 39, 17, 39, 61, 23, 53, 83, 29, 67, 105, 35, 81, 127,
    41, 95, 149, 47, 109, 171, 53, 123, 193, 59, 137, 215, 65, 151, 237, 71,
    165, 259, 77, 179, 281, 83, 193, 303, 89, 207, 325, 95, 221, 347.
]
self._VerifyValues(
    input_sizes=[1, 4, 4, 3],
    filter_sizes=[1, 1, 3, 2],
    out_backprop_sizes=[1, 4, 4, 2],
    strides=[1, 1],
    padding="VALID",
    data_format_src="NHWC",
    data_format_dst=data_format,
    expected=expected_output)
