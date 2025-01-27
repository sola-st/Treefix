# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/identify_dilated_conv1d.py
input_shape = parameters["input_shape"]
filter_size = parameters["filter_size"]
filter_shape = [filter_size, input_shape[2], parameters["num_filters"]]
exit([input_shape, filter_shape])
