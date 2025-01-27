# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/conv2d_test.py
self._VerifyValues(
    input_sizes=[1, 2, 3, 3],
    filter_sizes=[1, 2, 3, 3],
    strides=[1, 1],
    dilations=[2, 1],
    padding="VALID",
    data_format_src="NHWC",
    data_format_dst=data_format,
    expected=np.array([[[[231, 252, 273], [384, 423, 462]],
                        [[690, 765, 840], [843, 936, 1029]]]]))
