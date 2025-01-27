# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/gelu.py
values = [
    create_tensor_data(
        parameters["input_dtype"],
        parameters["input_shape"],
        min_value=-8,
        max_value=8)
]
exit((values, sess.run(outputs, feed_dict=dict(zip(inputs, values)))))
