# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/identify_dilated_conv1d.py
"""Build a conv graph given `parameters`."""
input_shape, filter_shape = get_tensor_shapes(parameters)
filter_input = tf.compat.v1.placeholder(
    dtype=tf.float32, name="filter", shape=filter_shape)
input_tensor = tf.compat.v1.placeholder(
    dtype=tf.float32, name="input", shape=input_shape)
input_tensors = [input_tensor, filter_input]

out = tf.nn.conv1d(
    input=input_tensor,
    filters=filter_input,
    stride=parameters["stride"],
    dilations=parameters["dilations"],
    padding=parameters["padding"])
exit((input_tensors, [out]))
