# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/greater_equal.py
"""Build the greater_equal op testing graph."""
input_value1 = tf.compat.v1.placeholder(
    dtype=parameters["input_dtype"],
    name="input1",
    shape=parameters["input_shape_pair"][0])
input_value2 = tf.compat.v1.placeholder(
    dtype=parameters["input_dtype"],
    name="input2",
    shape=parameters["input_shape_pair"][1])
out = tf.greater_equal(input_value1, input_value2)
exit(([input_value1, input_value2], [out]))
