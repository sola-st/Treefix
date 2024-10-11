# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/conv2d_test.py
self._VerifyValues(
    input_sizes=[0, 2, 3, 3],
    filter_sizes=[1, 1, 3, 3],
    strides=[1, 1],
    dilations=[2, 1],
    padding="VALID",
    data_format_src="NHWC",
    data_format_dst=data_format,
    expected=np.zeros([0, 2, 3, 3]))
