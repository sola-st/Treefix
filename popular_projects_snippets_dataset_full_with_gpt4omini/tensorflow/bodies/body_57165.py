# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/minimum.py
"""Build the minimum op testing graph."""
input_tensor_1 = tf.compat.v1.placeholder(
    dtype=parameters["input_dtype"],
    name="input_1",
    shape=parameters["input_shape_1"])
input_tensor_2 = tf.compat.v1.placeholder(
    dtype=parameters["input_dtype"],
    name="input_2",
    shape=parameters["input_shape_2"])

out = tf.minimum(input_tensor_1, input_tensor_2)
exit(([input_tensor_1, input_tensor_2], [out]))
