# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/atan2.py
"""Build the atan2 op testing graph."""
input_value1 = tf.compat.v1.placeholder(
    dtype=parameters["input_dtype"],
    name="y",
    shape=parameters["input_shape"])
input_value2 = tf.compat.v1.placeholder(
    dtype=parameters["input_dtype"],
    name="x",
    shape=parameters["input_shape"])
out = tf.math.atan2(input_value1, input_value2)
exit(([input_value1, input_value2], [out]))
