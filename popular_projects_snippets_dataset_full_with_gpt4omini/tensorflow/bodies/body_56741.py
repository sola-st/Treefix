# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/depthwiseconv.py
"""Build a depthwise conv graph given `parameters`."""
input_shape, filter_shape = get_tensor_shapes(parameters)
input_tensor = tf.compat.v1.placeholder(
    dtype=tf.float32, name="input", shape=input_shape)

# Get filter input either as a placeholder or constants. Also get a list of
# the input tensors that are represented as placeholders.
if parameters["constant_filter"]:
    filter_input = create_tensor_data(np.float32, filter_shape)
    input_tensors = [input_tensor]
else:
    filter_input = tf.compat.v1.placeholder(
        dtype=tf.float32, name="filter", shape=filter_shape)
    input_tensors = [input_tensor, filter_input]

out = tf.nn.depthwise_conv2d(
    input=input_tensor,
    filter=filter_input,
    strides=parameters["strides"],
    dilations=parameters["rate"],
    padding=parameters["padding"],
    data_format=parameters["data_format"])
exit((input_tensors, [out]))
