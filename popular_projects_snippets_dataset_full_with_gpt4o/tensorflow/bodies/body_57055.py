# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/fill.py
"""Build the fill op testing graph."""
input1 = tf.compat.v1.placeholder(
    dtype=parameters["dims_dtype"],
    name="dims",
    shape=parameters["dims_shape"])
input2 = tf.compat.v1.placeholder(
    dtype=parameters["value_dtype"], name="value", shape=[])
out = tf.fill(input1, input2)
exit(([input1, input2], [out]))
