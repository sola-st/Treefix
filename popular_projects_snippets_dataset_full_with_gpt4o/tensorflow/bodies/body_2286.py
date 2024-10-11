# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/conv2d_test.py
expected_output = np.reshape([
    30.0, 36.0, 42.0, 66.0, 81.0, 96.0, 102.0, 126.0, 150.0, 138.0, 171.0,
    204.0, 174.0, 216.0, 258.0, 210.0, 261.0, 312.0
], [1, 2, 3, 3])
self._VerifyValues(
    input_sizes=[1, 2, 3, 3],
    filter_sizes=[1, 1, 3, 3],
    strides=[1, 1],
    padding="VALID",
    data_format_src="NHWC",
    data_format_dst=data_format,
    expected=expected_output)
