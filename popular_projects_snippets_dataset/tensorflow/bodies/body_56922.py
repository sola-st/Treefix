# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/scatter_nd.py
"""Build the scatter_nd op testing graph."""
indices = tf.compat.v1.placeholder(
    dtype=parameters["indices_dtype"],
    name="indices",
    shape=parameters["indices_shape"])
updates = tf.compat.v1.placeholder(
    dtype=parameters["updates_dtype"],
    name="updates",
    shape=parameters["updates_shape"])
shape = tf.compat.v1.placeholder(
    dtype=parameters["shape_dtype"],
    name="shape",
    shape=parameters["shape_shape"])
out = tf.scatter_nd(indices, updates, shape)
exit(([indices, updates, shape], [out]))
