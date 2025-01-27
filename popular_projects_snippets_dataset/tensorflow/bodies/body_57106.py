# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/tensor_scatter_add.py
"""Build the tensor_scatter_add op testing graph."""
input_tensor = tf.compat.v1.placeholder(
    dtype=parameters["input_dtype"],
    name="input",
    shape=parameters["input_shape"])
# The indices will be a list of "input_shape".
indices_tensor = tf.compat.v1.placeholder(
    dtype=tf.int32,
    name="indices",
    shape=([parameters["adds_count"],
            len(parameters["input_shape"])]))
# The adds will be a list of scalar, shaped of "adds_count".
adds_tensors = tf.compat.v1.placeholder(
    dtype=parameters["input_dtype"],
    name="updates",
    shape=[parameters["adds_count"]])

out = tf.tensor_scatter_nd_add(input_tensor, indices_tensor, adds_tensors)
exit(([input_tensor, indices_tensor, adds_tensors], [out]))
