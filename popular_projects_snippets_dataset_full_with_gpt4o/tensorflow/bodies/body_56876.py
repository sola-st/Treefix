# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/tile.py
"""Build the tile op testing graph."""
input_value = tf.compat.v1.placeholder(
    dtype=parameters["input_dtype"],
    shape=parameters["input_shape"],
    name="input")
multiplier_value = tf.compat.v1.placeholder(
    dtype=parameters["multiplier_dtype"],
    shape=parameters["multiplier_shape"],
    name="multiplier")
out = tf.tile(input_value, multiplier_value)
exit(([input_value, multiplier_value], [out]))
