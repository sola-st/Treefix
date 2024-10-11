# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/cos.py
"""Build the cos op testing graph."""
input_tensor = tf.compat.v1.placeholder(
    dtype=parameters["input_dtype"],
    name="input",
    shape=parameters["input_shape"])

out = tf.cos(input_tensor)
exit(([input_tensor], [out]))
