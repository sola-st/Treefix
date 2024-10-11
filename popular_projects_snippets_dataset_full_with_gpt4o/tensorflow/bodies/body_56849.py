# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/broadcast_to.py
"""Build the graph for cond tests."""
input_tensor = tf.compat.v1.placeholder(
    dtype=parameters["input_dtype"],
    name="input",
    shape=parameters["input_shape"])

out = tf.broadcast_to(input_tensor, shape=parameters["output_shape"])
exit(([input_tensor], [out]))
