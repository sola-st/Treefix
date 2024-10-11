# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/conv2d_test.py
expected_output = np.reshape([
    231.0, 252.0, 273.0, 384.0, 423.0, 462.0, 690.0, 765.0, 840.0, 843.0,
    936.0, 1029.0
], [1, 2, 2, 3])
self._VerifyValues(
    input_sizes=[1, 2, 3, 3],
    filter_sizes=[1, 2, 3, 3],
    strides=[1, 1],
    padding="VALID",
    data_format_src="NHWC",
    data_format_dst=data_format,
    expected=expected_output)
