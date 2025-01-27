# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/transpose_conv.py
input_shape = parameters["input_shape"]
filter_size = parameters["filter_size"]
if not parameters["const_weight_bias"]:
    filter_shape = filter_size + [
        input_shape[3], parameters["channel_multiplier"]
    ]
    exit([input_shape, filter_shape])
exit([input_shape, filter_size])
