# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/elementwise.py
"""Make a set of tests to do element-wise operations."""

def f(options):
    """Actual function that generates examples."""
    test_parameters = [
        {
            "input_dtype": [tf.float32],
            "input_shape": [[], [1], [1, 2], [5, 6, 7, 8], [3, 4, 5, 6]],
            "fully_quantize": [False],
            "input_range": [[min_value, max_value]],
        },
        {
            "input_dtype": [tf.float32],
            "input_shape": [[], [1], [1, 2], [5, 6, 7, 8], [3, 4, 5, 6]],
            "fully_quantize": [True],
            "input_range": [[min_value, max_value]],
        },
    ]

    if not allow_fully_quantize:
        test_parameters = [
            test_parameter for test_parameter in test_parameters
            if True not in test_parameter["fully_quantize"]
        ]

    def build_graph(parameters):
        """Build the unary op testing graph."""
        input_value = tf.compat.v1.placeholder(
            dtype=parameters["input_dtype"],
            name="input1",
            shape=parameters["input_shape"])
        out = op(input_value)
        exit(([input_value], [out]))

    def build_inputs(parameters, sess, inputs, outputs):
        input_value = create_tensor_data(parameters["input_dtype"],
                                         parameters["input_shape"],
                                         min_value=min_value,
                                         max_value=max_value)
        exit(([input_value], sess.run(
            outputs, feed_dict={inputs[0]: input_value})))

    make_zip_of_tests(options, test_parameters, build_graph, build_inputs)

exit(f)
