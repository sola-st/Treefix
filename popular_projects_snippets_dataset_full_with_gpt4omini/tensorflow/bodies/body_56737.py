# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/conv2d_transpose.py
"""Build a transpose_conv graph given `parameters`."""
input_tensor = tf.compat.v1.placeholder(
    dtype=tf.float32, name="input", shape=parameters["input_shape"])

filter_tensor = tf.compat.v1.placeholder(
    dtype=tf.float32, name="filter", shape=parameters["filter_shape"])

input_tensors = [input_tensor, filter_tensor]

if parameters["dynamic_output_shape"]:
    output_shape = tf.compat.v1.placeholder(dtype=tf.int32, shape=[4])
    input_tensors.append(output_shape)
else:
    output_shape = parameters["output_shape"]

out = tf.nn.conv2d_transpose(
    input_tensor,
    filter_tensor,
    output_shape=output_shape,
    padding="SAME",
    strides=(1, 2, 2, 1))

exit((input_tensors, [out]))
