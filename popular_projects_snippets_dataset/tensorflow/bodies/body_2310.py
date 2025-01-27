# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/conv2d_test.py
self._VerifyValues(
    input_sizes=[0, 2, 3, 1],
    filter_sizes=[2, 2, 1, 1],
    out_backprop_sizes=[0, 1, 1, 1],
    strides=[1, 1],
    dilations=[1, 2],
    padding="VALID",
    data_format_src="NHWC",
    data_format_dst=data_format,
    expected=np.zeros([0]))
