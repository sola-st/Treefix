# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/conv2d_test.py
expected_output = np.array([[[[72], [82], [92]], [[112], [122], [132]]]])
self._VerifyValues(
    input_sizes=[1, 4, 4, 1],
    filter_sizes=[2, 2, 1, 1],
    strides=[1, 1],
    dilations=[2, 1],
    padding="VALID",
    data_format_src="NHWC",
    data_format_dst=data_format,
    expected=expected_output)
