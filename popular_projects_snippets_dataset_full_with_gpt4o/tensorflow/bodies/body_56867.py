# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/cast.py
"""Build the cast testing graph."""
input_value = tf.compat.v1.placeholder(
    dtype=parameters["input_dtype"],
    name="input",
    shape=parameters["input_shape"])
out = tf.cast(input_value, parameters["output_dtype"])
exit(([input_value], [out]))
