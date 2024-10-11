# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/conv_activation.py
"""Build a conv graph given `parameters`."""
input_shape, filter_shape = get_tensor_shapes(parameters)
input_tensor = tf.compat.v1.placeholder(
    dtype=tf.float32, name="input", shape=input_shape)

# Get filter input either as a placeholder or constants. Also get a list
# of the input tensors that are represented as placeholders.
if parameters["constant_filter"]:
    filter_input = create_tensor_data(
        np.float32, filter_shape, min_value=-10, max_value=10)
    input_tensors = [input_tensor]
else:
    filter_input = tf.compat.v1.placeholder(
        dtype=tf.float32, name="filter", shape=filter_shape)
    input_tensors = [input_tensor, filter_input]

out = tf.nn.conv2d(
    input=input_tensor,
    filters=filter_input,
    strides=parameters["strides"],
    dilations=parameters["dilations"],
    padding=parameters["padding"],
    data_format=parameters["data_format"])
out = activation_op(out)
exit((input_tensors, [out]))
