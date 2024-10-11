# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/prelu.py
"""Build the graph for the test case."""

input_tensor = tf.compat.v1.placeholder(
    dtype=tf.float32, name="input", shape=parameters["input_shape"])
prelu = tf.keras.layers.PReLU(shared_axes=parameters["shared_axes"])
out = prelu(input_tensor)
exit(([input_tensor], [out]))
