# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/minimum.py
"""Builds the inputs for the model above."""
values = [
    create_tensor_data(
        parameters["input_dtype"],
        parameters["input_shape_1"],
        min_value=-1,
        max_value=1),
    create_tensor_data(
        parameters["input_dtype"],
        parameters["input_shape_2"],
        min_value=-1,
        max_value=1)
]
exit((values, sess.run(outputs, feed_dict=dict(zip(inputs, values)))))
