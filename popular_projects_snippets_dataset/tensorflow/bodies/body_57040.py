# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/roll.py
input_value = create_tensor_data(
    parameters["input_dtype"], set_dynamic_shape(parameters["input_shape"]))
shift_value = get_value(parameters["shift"], np.int64)
axis_value = get_value(parameters["axis"], np.int64)
exit(([input_value, shift_value, axis_value], sess.run(
    outputs,
    feed_dict=dict(zip(inputs, [input_value, shift_value, axis_value])))))
