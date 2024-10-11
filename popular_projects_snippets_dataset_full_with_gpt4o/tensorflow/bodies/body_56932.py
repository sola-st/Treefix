# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/gelu.py
"""Builds the gelu op testing graph."""
input_tensor = tf.compat.v1.placeholder(
    dtype=parameters["input_dtype"],
    name="input",
    shape=parameters["input_shape"])

out = tf.nn.gelu(input_tensor, approximate=parameters["approximate"])
exit(([input_tensor], [out]))
