# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/expand_dims.py
"""Build the where op testing graph."""
inputs = []
input_value = tf.compat.v1.placeholder(
    dtype=parameters["input_type"],
    name="input",
    shape=parameters["input_shape"])
inputs.append(input_value)

if parameters["constant_axis"]:
    axis_value = tf.constant(
        parameters["axis_value"], dtype=tf.int32, shape=[1])
else:
    axis_value = tf.compat.v1.placeholder(
        dtype=tf.int32, name="axis", shape=[1])
    inputs.append(axis_value)

out = tf.expand_dims(input_value, axis=axis_value)
exit((inputs, [out]))
