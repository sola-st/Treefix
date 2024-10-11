# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/conv3d.py
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
        max_value=3)
]
exit((values, sess.run(outputs, feed_dict=dict(zip(inputs, values)))))
