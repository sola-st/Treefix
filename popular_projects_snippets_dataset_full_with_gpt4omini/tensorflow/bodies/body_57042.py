# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/expm1.py
"""Build the graph for the test case."""

input_tensor = tf.compat.v1.placeholder(
    dtype=tf.float32, name="input", shape=parameters["input_shape"])
out = tf.math.expm1(input_tensor)
exit(([input_tensor], [out]))
