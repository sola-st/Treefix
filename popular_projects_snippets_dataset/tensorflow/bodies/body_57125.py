# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/tensor_scatter_update.py
"""Build the tensor_scatter_update op testing graph."""
input_tensor = tf.compat.v1.placeholder(
    dtype=parameters["input_dtype"],
    name="input",
    shape=parameters["input_shape"])
# The indices will be a list of "input_shape".
indices_tensor = tf.compat.v1.placeholder(
    dtype=tf.int32,
    name="indices",
    shape=([parameters["updates_count"],
            len(parameters["input_shape"])]))
# The updates will be a list of scalar, shaped of "updates_count".
updates_tensors = tf.compat.v1.placeholder(
    dtype=parameters["input_dtype"],
    name="updates",
    shape=[parameters["updates_count"]])

out = tf.tensor_scatter_nd_update(input_tensor, indices_tensor,
                                  updates_tensors)
exit(([input_tensor, indices_tensor, updates_tensors], [out]))
