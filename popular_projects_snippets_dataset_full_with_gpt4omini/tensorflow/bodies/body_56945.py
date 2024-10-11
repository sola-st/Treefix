# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/conv_activation.py
"""Make a set of tests to do convolution with activation."""

def f(options):
    """Actual function that generates examples."""
    test_parameters = [
        {
            "input_shape": [[1, 3, 4, 3], [4, 6, 6, 1]],
            "filter_shape": [[1, 1], [2, 3], [3, 3]],
            "strides": [[1, 1, 1, 1], [1, 2, 3, 1]],
            "dilations": [[1, 1, 1, 1], [1, 3, 2, 1], [1, 2, 2, 1]],
            "padding": ["SAME", "VALID"],
            "data_format": ["NHWC"],  # TODO(aselle): NCHW  would be good
            "constant_filter": [True, False],
            "channel_multiplier": [1, 2],
            "fully_quantize": [False],
            "quant_16x8": [False],
            "dynamic_range_quantize": [False],
        },
        # TODO(b/134702301): The fully_quantize param is just ignored by the
        # MLIR testing path now, resulting in duplicate tests. Either ignore
        # these tests or handle it properly in the mlir_convert() function.
        {
            "input_shape": [[1, 3, 4, 3], [4, 6, 6, 1]],
            "filter_shape": [[1, 1], [2, 3]],
            "strides": [[1, 1, 1, 1], [1, 2, 3, 1]],
            "dilations": [[1, 1, 1, 1], [1, 3, 2, 1]],
            "padding": ["SAME", "VALID"],
            "data_format": ["NHWC"],  # TODO(aselle): NCHW  would be good
            "constant_filter": [True],
            "channel_multiplier": [1, 2],
            "fully_quantize": [True],
            "quant_16x8": [False, True],
            "dynamic_range_quantize": [False],
        },
        {
            "input_shape": [[1, 3, 4, 3]],
            "filter_shape": [[1, 1], [2, 3], [3, 3]],
            "strides": [[1, 1, 1, 1], [1, 2, 3, 1]],
            "dilations": [[1, 1, 1, 1]],
            "padding": ["SAME", "VALID"],
            "data_format": ["NHWC"],
            "constant_filter": [True],
            "channel_multiplier": [1, 2],
            "fully_quantize": [False],
            "quant_16x8": [False],
            "dynamic_range_quantize": [True],
        },
    ]

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

    def build_inputs(parameters, sess, inputs, outputs):
        """Build inputs for conv with activation."""

        input_shape, filter_shape = get_tensor_shapes(parameters)
        values = [
            create_tensor_data(
                np.float32, input_shape, min_value=-1, max_value=1)
        ]
        if not parameters["constant_filter"]:
            values.append(create_tensor_data(np.float32, filter_shape))
        exit((values, sess.run(outputs, feed_dict=dict(zip(inputs, values)))))

    make_zip_of_tests(
        options,
        test_parameters,
        build_graph,
        build_inputs,
        expected_tf_failures=48)

exit(f)
