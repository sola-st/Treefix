# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/conv2d_test.py
expected_output = [
    5, 17, 29, 25, 53, 81, 41, 53, 65, 109, 137, 165, 77, 89, 101, 193, 221,
    249, 113, 125, 137, 277, 305, 333
]
self._VerifyValues(
    input_sizes=[1, 2, 2, 6],
    filter_sizes=[2, 2, 3, 4],
    out_backprop_sizes=[1, 1, 1, 4],
    strides=[1, 1],
    padding="VALID",
    data_format_src="NHWC",
    data_format_dst=data_format,
    expected=expected_output)
