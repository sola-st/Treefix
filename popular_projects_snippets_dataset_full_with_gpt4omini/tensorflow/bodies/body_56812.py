# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/cumsum.py
"""Build the cumsum op testing graph."""
input1 = tf.compat.v1.placeholder(
    dtype=parameters["dtype"], shape=parameters["shape"])
out = tf.math.cumsum(
    input1,
    parameters["axis"],
    exclusive=parameters["exclusive"],
    reverse=parameters["reverse"])
exit(([input1], [out]))
