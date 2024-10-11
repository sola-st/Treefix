# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/expand_dims.py
"""Builds the inputs for expand_dims."""
input_values = []
input_values.append(
    create_tensor_data(
        parameters["input_type"],
        parameters["input_shape"],
        min_value=-1,
        max_value=1))
if not parameters["constant_axis"]:
    input_values.append(np.array([parameters["axis_value"]], dtype=np.int32))
exit((input_values, sess.run(
    outputs, feed_dict=dict(zip(inputs, input_values)))))
