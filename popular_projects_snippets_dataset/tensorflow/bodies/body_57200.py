# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/unique.py
"""Build the graph for the test case."""

input_tensor = tf.compat.v1.placeholder(
    dtype=tf.int32, name="input", shape=parameters["input_shape"])
if parameters["index_type"] is None:
    output = tf.unique(input_tensor)
else:
    output = tf.unique(input_tensor, parameters["index_type"])

exit(([input_tensor], output))
