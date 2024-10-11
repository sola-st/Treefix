# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/sparse_to_dense.py
"""Build the sparse_to_dense op testing graph."""
dense_shape = parameters["dense_shape"]

# Special handle for value_is_scalar case.
# value_count must be 1.
if parameters["value_is_scalar"] and parameters["value_count"] == 1:
    value = tf.compat.v1.placeholder(
        name="value", dtype=parameters["value_dtype"], shape=())
else:
    value = tf.compat.v1.placeholder(
        name="value",
        dtype=parameters["value_dtype"],
        shape=[parameters["value_count"]])
indices = set()
while len(indices) < parameters["value_count"]:
    indices.add(generate_index(dense_shape))
indices = tf.constant(tuple(indices), dtype=parameters["index_dtype"])
# TODO(renjieliu): Add test for validate_indices case.
out = tf.compat.v1.sparse_to_dense(
    indices,
    dense_shape,
    value,
    parameters["default_value"],
    validate_indices=False)

exit(([value], [out]))
