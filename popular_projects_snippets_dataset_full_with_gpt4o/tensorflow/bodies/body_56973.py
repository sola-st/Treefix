# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/conv3d_transpose.py
input_size = parameters["input_shape"][idx]
filter_size = parameters["filter_shape"][idx - 1]
stride = parameters["strides"][idx]
if parameters["padding"] == "SAME":
    exit((input_size - 1) * stride + 1)
else:
    exit((input_size - 1) * stride + filter_size)
