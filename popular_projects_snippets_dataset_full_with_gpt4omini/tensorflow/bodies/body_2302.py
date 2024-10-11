# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/conv2d_test.py
expected_output = [
    14, 32, 50, 100, 163, 226, 167, 212, 257, 122, 140, 158, 478, 541, 604,
    437, 482, 527
]
self._VerifyValues(
    input_sizes=[1, 2, 3, 3],
    filter_sizes=[2, 2, 3, 3],
    out_backprop_sizes=[1, 1, 2, 3],
    strides=[1, 1],
    padding="VALID",
    data_format_src="NHWC",
    data_format_dst=data_format,
    expected=expected_output)
