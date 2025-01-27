# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/shape_to_strided_slice.py
"""Build inputs for stride_slice test."""
input_values = create_tensor_data(
    parameters["dtype"],
    parameters["input_shape"],
    min_value=-1,
    max_value=1)
values = [input_values]

exit((values, sess.run(outputs, feed_dict=dict(zip(inputs, values)))))
