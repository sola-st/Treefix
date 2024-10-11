# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/conv2d_test.py
expected_output = np.reshape(
    [2271.0, 2367.0, 2463.0, 2901.0, 3033.0, 3165.0], [1, 1, 2, 3])
self._VerifyValues(
    input_sizes=[1, 2, 3, 3],
    filter_sizes=[2, 2, 3, 3],
    strides=[1, 1],
    padding="VALID",
    data_format_src="NHWC",
    data_format_dst=data_format,
    expected=expected_output)
