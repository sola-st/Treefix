# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/embedding_lookup.py
"""Build the gather op testing graph."""
params = tf.compat.v1.placeholder(
    dtype=parameters["params_dtype"],
    name="params",
    shape=parameters["params_shape"])
ids = tf.compat.v1.placeholder(
    dtype=parameters["ids_dtype"],
    name="ids",
    shape=parameters["ids_shape"])
out = tf.nn.embedding_lookup(params=params, ids=ids)
exit(([params, ids], [out]))
