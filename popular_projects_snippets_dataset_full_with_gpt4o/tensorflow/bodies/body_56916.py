# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/conv_to_depthwiseconv_with_shared_weights.py
"""Build a conv graph given `parameters`."""
input_shape, filter_shape = get_tensor_shapes(parameters)
input_tensor = tf.compat.v1.placeholder(
    dtype=tf.float32, name="input", shape=input_shape)

# Construct a constant weights tensor which will be used by both Conv2D.
filter_tensor = tf.constant(
    create_tensor_data(np.float32, filter_shape), dtype=tf.float32)
input_tensors = [input_tensor]

# Construct 2 Conv2D operations which use exactly the same input and
# weights.
result1 = tf.nn.conv2d(
    input=input_tensor,
    filters=filter_tensor,
    strides=parameters["strides"],
    dilations=parameters["dilations"],
    padding=parameters["padding"],
    data_format=parameters["data_format"])
result2 = tf.nn.conv2d(
    input=input_tensor,
    filters=filter_tensor,
    strides=parameters["strides"],
    dilations=parameters["dilations"],
    padding=parameters["padding"],
    data_format=parameters["data_format"])
# Add the 2 results up.
out = result1 + result2
exit((input_tensors, [out]))
