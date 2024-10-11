# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/less_equal.py
input_shape_1 = populate_dynamic_shape(parameters,
                                       parameters["input_shape_pair"][0])
input_shape_2 = populate_dynamic_shape(parameters,
                                       parameters["input_shape_pair"][1])

input_value1 = create_tensor_data(parameters["input_dtype"], input_shape_1)
input_value2 = create_tensor_data(parameters["input_dtype"], input_shape_2)
exit(([input_value1, input_value2], sess.run(
    outputs, feed_dict=dict(zip(inputs, [input_value1, input_value2])))))
