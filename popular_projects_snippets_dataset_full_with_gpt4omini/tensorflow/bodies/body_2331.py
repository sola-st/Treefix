# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/conv2d_test.py
self._VerifyValues(
    input_sizes=[1, 3, 4, 3],
    filter_sizes=[2, 2, 3, 3],
    out_backprop_sizes=[1, 1, 2, 3],
    strides=[1, 1],
    dilations=[2, 2],
    padding="VALID",
    data_format_src="NHWC",
    data_format_dst=data_format,
    expected=[
        17, 22, 27, 22, 29, 36, 27, 36, 45, 47, 64, 81, 52, 71, 90, 57, 78,
        99, 137, 190, 243, 142, 197, 252, 147, 204, 261, 167, 232, 297, 172,
        239, 306, 177, 246, 315
    ])
