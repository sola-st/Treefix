# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/shape.py
input_value = create_tensor_data(parameters["input_dtype"],
                                 parameters["input_shape"])
new_shape = np.array(parameters["new_shape"])
exit(([input_value, new_shape], sess.run(
    outputs, feed_dict=dict(zip(inputs, [input_value, new_shape])))))
