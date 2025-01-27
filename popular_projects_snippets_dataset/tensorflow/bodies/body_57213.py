# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/reciprocal.py
"""Build the graph for cond tests."""
input_tensor = tf.compat.v1.placeholder(
    dtype=parameters["input_dtype"],
    name="input",
    shape=parameters["input_shape"])

out = tf.math.reciprocal(input_tensor)
exit(([input_tensor], [out]))
