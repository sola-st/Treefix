# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/rank.py
"""Build the rank op testing graph."""
input_value = tf.compat.v1.placeholder(
    dtype=parameters["input_dtype"], name="input")
out = tf.rank(input_value)
exit(([input_value], [out]))
