# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/conv_bias_activation.py
"""Build a conv graph given `parameters`."""
input_shape, filter_shape = get_tensor_shapes(parameters)
input_tensor = tf.compat.v1.placeholder(
    dtype=tf.float32, name="input", shape=input_shape)

filter_input = create_tensor_data(
    np.float32, filter_shape, min_value=-10, max_value=10)
input_tensors = [input_tensor]

if parameters["data_format"] == "NCHW":
    out = add_conv(input_tensor, filter_input, parameters)
else:
    out = tf.nn.conv2d(
        input=input_tensor,
        filters=filter_input,
        strides=parameters["strides"],
        dilations=parameters["dilations"],
        padding="VALID",
        data_format=parameters["data_format"])
out = add_bias_add(out, filter_shape)
out = activation_op(out)

# Add another conv + bias_add + activation.

# Create constant filter for the second conv2d.
filter_input_2 = create_tensor_data(
    np.float32, parameters["filter_2_shape"], min_value=-10, max_value=10)
if parameters["data_format"] == "NCHW":
    out = add_conv(out, filter_input_2, parameters)
else:
    out = tf.nn.conv2d(
        input=out,
        filters=filter_input_2,
        strides=parameters["strides"],
        dilations=parameters["dilations"],
        padding="VALID",
        data_format=parameters["data_format"])
out = add_bias_add(out, filter_shape)
out = activation_op(out)
exit((input_tensors, [out]))
