# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/nearest_upsample.py
"""Build the nearest upsample testing graph."""
input_shape = parameters["input_shape"]
input_tensor = tf.compat.v1.placeholder(
    dtype=parameters["dtype"], name="input", shape=input_shape)
scales, axis = parameters["scale_n_axis"]
input_new_shape, ones_new_shape, new_shape = new_shape_for_upsample(
    input_shape, scales, axis)

out = tf.compat.v1.reshape(input_tensor,
                           input_new_shape) * tf.compat.v1.ones(
                               ones_new_shape, dtype=parameters["dtype"])
out = tf.compat.v1.reshape(out, new_shape)
exit(([input_tensor], [out]))
