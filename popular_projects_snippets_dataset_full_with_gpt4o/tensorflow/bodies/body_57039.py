# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/roll.py
input_tensor = tf.compat.v1.placeholder(
    dtype=parameters["input_dtype"],
    name="input",
    shape=parameters["input_shape"])
shift_tensor = tf.compat.v1.placeholder(
    dtype=tf.int64, name="shift", shape=get_shape(parameters["shift"]))
axis_tensor = tf.compat.v1.placeholder(
    dtype=tf.int64, name="axis", shape=get_shape(parameters["axis"]))
outs = tf.roll(input_tensor, shift_tensor, axis_tensor)
exit(([input_tensor, shift_tensor, axis_tensor], [outs]))
