# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/leaky_relu.py
"""Build the graph for the test case."""

input_tensor = tf.compat.v1.placeholder(
    dtype=tf.float32, name="input", shape=parameters["input_shape"])
out = tf.nn.leaky_relu(input_tensor, alpha=parameters["alpha"])
exit(([input_tensor], [out]))
