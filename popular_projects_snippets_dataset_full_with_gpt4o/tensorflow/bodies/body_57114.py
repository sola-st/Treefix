# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/matrix_band_part.py
static_input_shape = get_static_shape(parameters["input_shape"])
input_value = create_tensor_data(parameters["input_dtype"],
                                 static_input_shape)
num_lower = create_tensor_data(
    parameters["index_dtype"],
    shape=(),
    min_value=-1,
    max_value=static_input_shape[-2])
num_upper = create_tensor_data(
    parameters["index_dtype"],
    shape=(),
    min_value=-1,
    max_value=static_input_shape[-1])
exit(([input_value, num_lower, num_upper
       ], sess.run(outputs,
                   dict(zip(inputs, [input_value, num_lower, num_upper])))))
