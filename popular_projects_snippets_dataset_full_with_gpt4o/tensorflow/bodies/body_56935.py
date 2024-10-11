# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/gather_nd.py
"""Build the gather_nd op testing graph."""
params = tf.compat.v1.placeholder(
    dtype=parameters["params_dtype"],
    name="params",
    shape=parameters["params_shape"])
indices = tf.compat.v1.placeholder(
    dtype=parameters["indices_dtype"],
    name="indices",
    shape=parameters["indices_shape"])
out = tf.gather_nd(params, indices)
exit(([params, indices], [out]))
