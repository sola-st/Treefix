# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/cos.py
values = [
    create_tensor_data(
        parameters["input_dtype"],
        parameters["input_shape"],
        min_value=-np.pi,
        max_value=np.pi)
]
exit((values, sess.run(outputs, feed_dict=dict(zip(inputs, values)))))
