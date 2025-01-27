# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/identify_dilated_conv1d.py
input_shape, filter_shape = get_tensor_shapes(parameters)
values = [
    create_tensor_data(np.float32, input_shape, min_value=-1, max_value=1),
    create_tensor_data(np.float32, filter_shape)
]

exit((values, sess.run(outputs, feed_dict=dict(zip(inputs, values)))))
