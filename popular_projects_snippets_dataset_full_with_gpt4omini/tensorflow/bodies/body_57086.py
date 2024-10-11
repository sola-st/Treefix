# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/conv_with_shared_weights.py
"""Build a conv graph given `parameters`."""
input_shape, filter_shape = get_tensor_shapes(parameters)
input_tensor = tf.compat.v1.placeholder(
    dtype=tf.float32, name="input", shape=input_shape)
input_tensors = [input_tensor]

# Construct a constant weights tensor which will be used by both Conv2D.
filter_tensor = tf.constant(
    create_tensor_data(np.float32, filter_shape), dtype=tf.float32)

# Ensure that FuseBinaryIntoFollowingAffine works with an input which
# is shared by multiple affine ops.
conv_input = input_tensor + 0.1

# Construct 2 Conv2D operations which use exactly the same input and
# weights.
result1 = tf.nn.conv2d(
    input=conv_input,
    filters=filter_tensor,
    strides=parameters["strides"],
    dilations=parameters["dilations"],
    padding=parameters["padding"],
    data_format=parameters["data_format"])
result2 = tf.nn.conv2d(
    input=conv_input,
    filters=filter_tensor,
    strides=parameters["strides"],
    dilations=parameters["dilations"],
    padding=parameters["padding"],
    data_format=parameters["data_format"])
# Add MUL ops after Conv2D ops. These MUL ops should be fused into the
# weights of Conv2D.
result1 = result1 * 2
result2 = result2 * 3
# Add the 2 results up.
out = result1 + result2
exit((input_tensors, [out]))
