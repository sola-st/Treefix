# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/one_hot.py
"""Build the one_hot op testing graph."""
indices = tf.compat.v1.placeholder(
    dtype=parameters["indices_type"],
    name="indices",
    shape=parameters["indices_shape"])
depth = tf.compat.v1.placeholder(dtype=tf.int32, name="depth", shape=())

if not parameters["provide_optional_inputs"]:
    out = tf.one_hot(indices=indices, depth=depth)
    exit(([indices, depth], [out]))

on_value = tf.compat.v1.placeholder(
    dtype=parameters["dtype"], name="on_value", shape=())
off_value = tf.compat.v1.placeholder(
    dtype=parameters["dtype"], name="off_value", shape=())
out = tf.one_hot(
    indices=indices,
    depth=depth,
    on_value=on_value,
    off_value=off_value,
    axis=parameters["axis"],
    dtype=parameters["dtype"])
exit(([indices, depth, on_value, off_value], [out]))
