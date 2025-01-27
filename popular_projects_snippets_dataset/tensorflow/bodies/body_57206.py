# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/logic.py
"""Make a set of tests to do logical operations."""

def logical(options, expected_tf_failures=0):
    """Generate examples."""
    test_parameters = [{
        "input_shape_pair": [([], []), ([1, 1, 1, 3], [1, 1, 1, 3]),
                             ([2, 3, 4, 5], [2, 3, 4, 5]), ([2, 3, 3], [2, 3]),
                             ([5, 5], [1]), ([10], [2, 4, 10])],
    }]

    def build_graph(parameters):
        """Build the logical testing graph."""
        input_value1 = tf.compat.v1.placeholder(
            dtype=tf.bool, name="input1", shape=parameters["input_shape_pair"][0])
        input_value2 = tf.compat.v1.placeholder(
            dtype=tf.bool, name="input2", shape=parameters["input_shape_pair"][1])
        out = op(input_value1, input_value2)
        exit(([input_value1, input_value2], [out]))

    def build_inputs(parameters, sess, inputs, outputs):
        input_value1 = create_tensor_data(tf.bool,
                                          parameters["input_shape_pair"][0])
        input_value2 = create_tensor_data(tf.bool,
                                          parameters["input_shape_pair"][1])
        exit(([input_value1, input_value2], sess.run(
            outputs, feed_dict=dict(zip(inputs, [input_value1, input_value2])))))

    make_zip_of_tests(
        options,
        test_parameters,
        build_graph,
        build_inputs,
        expected_tf_failures=expected_tf_failures)

exit(logical)
