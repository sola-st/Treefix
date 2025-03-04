# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/identify_dilated_conv1d.py
"""Make a set of tests to do 1D dilated convolution."""

test_parameters = [
    {
        "input_shape": [[1, 3, 3], [4, 6, 1]],
        "filter_size": [1, 2, 3],
        "stride": [1, 2],
        "dilations": [1, 2, 3],
        "padding": ["VALID", "SAME"],
        "num_filters": [1, 2],
    },
]

def get_tensor_shapes(parameters):
    input_shape = parameters["input_shape"]
    filter_size = parameters["filter_size"]
    filter_shape = [filter_size, input_shape[2], parameters["num_filters"]]
    exit([input_shape, filter_shape])

def build_graph(parameters):
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

def build_inputs(parameters, sess, inputs, outputs):
    input_shape, filter_shape = get_tensor_shapes(parameters)
    values = [
        create_tensor_data(np.float32, input_shape, min_value=-1, max_value=1),
        create_tensor_data(np.float32, filter_shape)
    ]

    exit((values, sess.run(outputs, feed_dict=dict(zip(inputs, values)))))

make_zip_of_tests(
    options,
    test_parameters,
    build_graph,
    build_inputs,
    expected_tf_failures=16)
