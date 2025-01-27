# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/matrix_set_diag.py
input_shape = parameters["input_diag_shapes"][0]
diag_shape = parameters["input_diag_shapes"][1]
input_values = create_tensor_data(parameters["input_dtype"], input_shape)
diag_values = create_tensor_data(parameters["input_dtype"], diag_shape)
exit(([input_values, diag_values], sess.run(
    outputs, feed_dict=dict(zip(inputs, [input_values, diag_values])))))
