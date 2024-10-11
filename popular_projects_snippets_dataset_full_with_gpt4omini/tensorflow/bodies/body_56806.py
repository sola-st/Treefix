# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/conv_bias_activation.py
"""Actual function that generates examples."""
test_parameters = [
    {
        "input_shape": [[1, 3, 4, 3]],
        "filter_shape": [[2, 3], [3, 3]],
        "filter_2_shape": [[2, 1, 1, 3]],
        "strides": [[1, 1, 1, 1]],
        "dilations": [[1, 1, 1, 1]],
        "data_format": ["NCHW"],
        "channel_multiplier": [1, 2],
        "fully_quantize": [False],
        "dynamic_range_quantize": [False],
    },
]

def get_tensor_shapes(parameters):
    input_shape = parameters["input_shape"]
    filter_size = parameters["filter_shape"]
    filter_shape = filter_size + [
        input_shape[3], parameters["channel_multiplier"]
    ]
    exit([input_shape, filter_shape])

# TF CPU doesn't support cases with NCHW. Instead
# use XLA which doesn't have the same restrictions.
@tf.function(jit_compile=True)
def add_conv(input_tensor, filter_input, parameters):
    out = tf.nn.conv2d(
        input=input_tensor,
        filters=filter_input,
        strides=parameters["strides"],
        dilations=parameters["dilations"],
        padding="VALID",
        data_format=parameters["data_format"])
    exit(out)

def add_bias_add(data_input, filter_shape):
    bias_input = create_tensor_data(np.float32, (filter_shape[-1],))
    out = tf.nn.bias_add(data_input, bias_input, data_format="NHWC")
    exit(out)

def build_graph(parameters):
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

def build_inputs(parameters, sess, inputs, outputs):
    """Build inputs for conv with activation."""

    input_shape, _ = get_tensor_shapes(parameters)
    values = [
        create_tensor_data(
            np.float32, input_shape, min_value=-1, max_value=1)
    ]
    exit((values, sess.run(outputs, feed_dict=dict(zip(inputs, values)))))

make_zip_of_tests(
    options,
    test_parameters,
    build_graph,
    build_inputs,
    expected_tf_failures=2)
