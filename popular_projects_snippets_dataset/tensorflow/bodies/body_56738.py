# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/conv2d_transpose.py
values = [
    create_tensor_data(np.float32, parameters["input_shape"]),
    create_tensor_data(np.float32, parameters["filter_shape"])
]
if parameters["dynamic_output_shape"]:
    values.append(np.array(parameters["output_shape"]))

exit((values, sess.run(outputs, feed_dict=dict(zip(inputs, values)))))
