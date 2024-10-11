# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/conv2d_test.py
# The GPU version of this test is not very stable. So adjusting the
# error threshold to 1e-4.
self._VerifyValues(
    input_sizes=[1, 3, 2, 3],
    filter_sizes=[2, 2, 3, 3],
    out_backprop_sizes=[1, 1, 1, 3],
    strides=[1, 1],
    dilations=[2, 1],
    padding="VALID",
    data_format_src="NHWC",
    data_format_dst=data_format,
    expected=[
        14, 32, 50, 68, 86, 104, 0, 0, 0, 0, 0, 0, 122, 140, 158, 176, 194,
        212
    ])
