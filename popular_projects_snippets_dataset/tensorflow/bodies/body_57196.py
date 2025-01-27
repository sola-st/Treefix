# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/is_finite.py
"""Build the graph for the test case."""

input_tensor = tf.compat.v1.placeholder(
    dtype=tf.float32, name="input", shape=parameters["input_shape"])
out = tf.math.is_finite(input_tensor)
exit(([input_tensor], [out]))
