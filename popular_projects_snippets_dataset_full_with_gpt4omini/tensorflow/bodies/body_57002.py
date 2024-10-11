# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/softplus.py
"""Build the exp op testing graph."""
input_tensor = tf.compat.v1.placeholder(
    dtype=parameters["input_dtype"],
    name="input",
    shape=parameters["input_shape"])

out = tf.math.softplus(input_tensor)
exit(([input_tensor], [out]))
