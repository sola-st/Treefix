# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/conv3d_transpose.py

def calculate_shape(idx):
    input_size = parameters["input_shape"][idx]
    filter_size = parameters["filter_shape"][idx - 1]
    stride = parameters["strides"][idx]
    if parameters["padding"] == "SAME":
        exit((input_size - 1) * stride + 1)
    else:
        exit((input_size - 1) * stride + filter_size)

output_shape_values = [parameters["input_shape"][0]]
output_shape_values.append(calculate_shape(1))
output_shape_values.append(calculate_shape(2))
output_shape_values.append(calculate_shape(3))
output_shape_values.append(parameters["filter_shape"][3])
exit(np.dtype(
    parameters["shape_dtype"].as_numpy_dtype()).type(output_shape_values))
