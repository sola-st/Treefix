# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/reshape.py
"""Build inputs for reshape op."""

values = [
    create_tensor_data(
        parameters["dtype"],
        parameters["input_shape"],
        min_value=-1,
        max_value=1)
]
if not parameters["constant_shape"]:
    values.append(np.array(parameters["output_shape"]))

exit((values, sess.run(outputs, feed_dict=dict(zip(inputs, values)))))
