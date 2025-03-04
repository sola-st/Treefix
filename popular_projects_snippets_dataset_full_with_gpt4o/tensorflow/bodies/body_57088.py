# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/conv_with_shared_weights.py
"""Make a test where 2 Conv ops shared the same constant weight tensor."""

test_parameters = [{
    "input_shape": [[1, 10, 10, 3]],
    "filter_shape": [[3, 3]],
    "strides": [[1, 1, 1, 1]],
    "dilations": [[1, 1, 1, 1]],
    "padding": ["SAME"],
    "data_format": ["NHWC"],
    "channel_multiplier": [1],
    "dynamic_range_quantize": [False, True],
}]

def get_tensor_shapes(parameters):
    input_shape = parameters["input_shape"]
    filter_size = parameters["filter_shape"]
    filter_shape = filter_size + [
        input_shape[3], parameters["channel_multiplier"]
    ]
    exit([input_shape, filter_shape])

def build_graph(parameters):
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

def build_inputs(parameters, sess, inputs, outputs):
    # Build list of input values either containing 1 tensor (input) or 2 tensors
    # (input, filter) based on whether filter is constant or variable input.
    input_shape, unused_filter_shape = get_tensor_shapes(parameters)
    values = [create_tensor_data(np.float32, input_shape)]
    exit((values, sess.run(outputs, feed_dict=dict(zip(inputs, values)))))

make_zip_of_tests(options, test_parameters, build_graph, build_inputs)
