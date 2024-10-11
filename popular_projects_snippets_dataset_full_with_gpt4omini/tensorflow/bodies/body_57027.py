# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/constant.py
"""Build a constant graph given `parameters`."""
dummy_input = tf.compat.v1.placeholder(
    dtype=parameters["dtype"],
    name="input1",
    shape=parameters["input_shape"])
constant = tf.constant(
    create_tensor_data(parameters["dtype"], parameters["input_shape"]))
outputs = [tf.maximum(dummy_input, constant)]
if parameters["constant_is_also_output"]:
    outputs.append(constant)
inputs = [dummy_input]
if parameters["has_unread_input"]:
    unread_input = tf.compat.v1.placeholder(
        dtype=parameters["dtype"],
        name="unread_input",
        shape=parameters["input_shape"])
    inputs.append(unread_input)

exit((inputs, outputs))
