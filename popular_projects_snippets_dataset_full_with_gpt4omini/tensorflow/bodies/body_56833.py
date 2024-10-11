# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/transpose_conv.py
"""Make a set of tests to do transpose_conv."""

# Tensorflow only supports equal strides
test_parameters = [
    {
        "input_shape": [[1, 3, 4, 1], [1, 10, 10, 3], [3, 20, 20, 1]],
        "filter_size": [[1, 1], [1, 2], [3, 3]],
        "has_bias": [False],
        "strides": [[1, 1, 1, 1], [1, 3, 3, 1]],
        "padding": ["SAME", "VALID"],
        "data_format": ["NHWC"],
        "channel_multiplier": [1, 2],
        "output_shape": [[]],
        "fully_quantize": [False],
        "const_weight_bias": [False]
    },
    # TODO(yunluli): Adding simple tests for now to unblock edgetpu debugging.
    # Need to add more test cases.
    {
        "input_shape": [[1, 3, 3, 1]],
        "filter_size": [[3, 3, 2, 1]],
        "has_bias": [False],
        "strides": [[1, 1, 1, 1]],
        "padding": ["SAME"],
        "data_format": ["NHWC"],
        "channel_multiplier": [1],
        "output_shape": [[1, 3, 3, 2]],
        "fully_quantize": [True],
        "const_weight_bias": [True]
    },
    {
        "input_shape": [[1, 3, 3, 1]],
        "filter_size": [[3, 3, 2, 1]],
        "has_bias": [False],
        "strides": [[1, 1, 1, 1]],
        "padding": ["SAME"],
        "data_format": ["NHWC"],
        "channel_multiplier": [1],
        "output_shape": [[1, 3, 3, 2]],
        "fully_quantize": [False],
        "const_weight_bias": [True]
    },
    {
        "input_shape": [[1, 3, 3, 1]],
        "filter_size": [[3, 3, 2, 1]],
        "has_bias": [False],
        "strides": [[1, 2, 2, 1]],
        "padding": ["SAME"],
        "data_format": ["NHWC"],
        "channel_multiplier": [1],
        "output_shape": [[1, 6, 6, 2]],
        "fully_quantize": [True],
        "const_weight_bias": [True]
    },
    {
        "input_shape": [[1, 4, 3, 1]],
        "filter_size": [[3, 3, 2, 1]],
        "has_bias": [False],
        "strides": [[1, 2, 2, 1]],
        "padding": ["SAME"],
        "data_format": ["NHWC"],
        "channel_multiplier": [1],
        "output_shape": [[1, 8, 6, 2]],
        "fully_quantize": [True],
        "const_weight_bias": [True]
    },
    {
        "input_shape": [[1, 3, 3, 1]],
        "filter_size": [[3, 3, 2, 1]],
        "has_bias": [True],
        "strides": [[1, 1, 1, 1]],
        "padding": ["SAME"],
        "data_format": ["NHWC"],
        "channel_multiplier": [1],
        "output_shape": [[1, 3, 3, 2]],
        "fully_quantize": [True],
        "const_weight_bias": [True]
    },
]

def get_tensor_shapes(parameters):
    input_shape = parameters["input_shape"]
    filter_size = parameters["filter_size"]
    if not parameters["const_weight_bias"]:
        filter_shape = filter_size + [
            input_shape[3], parameters["channel_multiplier"]
        ]
        exit([input_shape, filter_shape])
    exit([input_shape, filter_size])

def build_graph(parameters):
    """Build a transpose_conv graph given `parameters`."""
    input_shape, filter_shape = get_tensor_shapes(parameters)
    input_tensor = tf.compat.v1.placeholder(
        dtype=tf.float32, name="input", shape=input_shape)

    filter_input = tf.compat.v1.placeholder(
        dtype=tf.float32, name="filter", shape=filter_shape)

    if not parameters["const_weight_bias"]:
        input_tensors = [input_tensor, filter_input]
        conv_outputs = tf.nn.conv2d(
            input=input_tensor,
            filters=filter_input,
            strides=parameters["strides"],
            padding=parameters["padding"],
            data_format=parameters["data_format"])
        out = tf.compat.v1.nn.conv2d_backprop_input(
            input_shape,
            filter_input,
            conv_outputs,
            strides=parameters["strides"],
            padding=parameters["padding"],
            data_format=parameters["data_format"])
    else:
        input_tensors = [input_tensor]
        if parameters["fully_quantize"]:
            filter_input = create_tensor_data(
                np.float32, filter_shape, min_value=-1, max_value=1)
        else:
            filter_input = create_tensor_data(np.float32, filter_shape)
        out = tf.nn.conv2d_transpose(
            input_tensor,
            filter_input,
            parameters["output_shape"],
            strides=parameters["strides"],
            padding=parameters["padding"],
            data_format=parameters["data_format"])
        if parameters["has_bias"]:
            if parameters["fully_quantize"]:
                bias_input = create_tensor_data(
                    np.float32, (parameters["output_shape"][-1],),
                    min_value=-1,
                    max_value=1)
            else:
                bias_input = create_tensor_data(np.float32,
                                                (parameters["output_shape"][-1],))
            out = tf.nn.bias_add(
                out, bias_input, data_format=parameters["data_format"])

            mul_data = create_tensor_data(np.float32,
                                          (parameters["output_shape"][-1],))
            out = tf.math.multiply(out, mul_data)

    exit((input_tensors, [out]))

def build_inputs(parameters, sess, inputs, outputs):
    input_shape, filter_shape = get_tensor_shapes(parameters)
    if not parameters["const_weight_bias"]:
        values = [
            create_tensor_data(np.float32, input_shape),
            create_tensor_data(np.float32, filter_shape)
        ]
    else:
        if parameters["fully_quantize"]:
            values = [
                create_tensor_data(
                    np.float32, input_shape, min_value=-1, max_value=1),
            ]
        else:
            values = [create_tensor_data(np.float32, input_shape),]

    exit((values, sess.run(outputs, feed_dict=dict(zip(inputs, values)))))

make_zip_of_tests(options, test_parameters, build_graph, build_inputs)
