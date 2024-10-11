# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/conv.py
input_shape = parameters["input_shape"]
filter_size = parameters["filter_shape"]
filter_shape = filter_size + [
    input_shape[3], parameters["channel_multiplier"]
]
exit([input_shape, filter_shape])
