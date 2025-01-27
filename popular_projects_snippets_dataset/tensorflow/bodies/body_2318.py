# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/conv2d_test.py
expected_output = [
    17, 22, 27, 22, 29, 36, 27, 36, 45, 32, 43, 54, 37, 50, 63, 42, 57, 72,
    62, 85, 108, 67, 92, 117, 72, 99, 126, 77, 106, 135, 82, 113, 144, 87,
    120, 153
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
