# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/conv3d_transpose.py
values = [
    create_tensor_data(
        parameters["input_dtype"],
        parameters["input_shape"],
        min_value=-100,
        max_value=9),
    create_tensor_data(
        parameters["input_dtype"],
        parameters["filter_shape"],
        min_value=-3,
        max_value=3),
    calculate_output_shape(parameters)
]
exit((values, sess.run(outputs, feed_dict=dict(zip(inputs, values)))))
