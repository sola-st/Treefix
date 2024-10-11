# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/pad.py
"""Build inputs for pad op."""

values = [
    create_tensor_data(
        parameters["dtype"],
        parameters["input_shape"],
        min_value=-1,
        max_value=1)
]
if not parameters["constant_paddings"]:
    values.append(np.array(parameters["paddings"]))
exit((values, sess.run(outputs, feed_dict=dict(zip(inputs, values)))))
