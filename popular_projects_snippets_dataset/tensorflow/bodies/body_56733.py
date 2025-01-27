# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/leaky_relu.py
"""Make a set of tests to do LeakyRelu."""

test_parameters = [{
    "input_shape": [[], [1], [5], [1, 10, 10, 3], [3, 3, 3, 3]],
    "alpha": [0.1, 1.0, 2.0, -0.1, -1.0, -2.0],
    "fully_quantize": [False, True],
    "input_range": [(-3, 10)],
    "quant_16x8": [False, True],
}]

def build_graph(parameters):
    """Build the graph for the test case."""

    input_tensor = tf.compat.v1.placeholder(
        dtype=tf.float32, name="input", shape=parameters["input_shape"])
    out = tf.nn.leaky_relu(input_tensor, alpha=parameters["alpha"])
    exit(([input_tensor], [out]))

def build_inputs(parameters, sess, inputs, outputs):
    """Build the inputs for the test case."""
    input_values = create_tensor_data(
        np.float32, parameters["input_shape"], min_value=-3, max_value=10)
    exit(([input_values], sess.run(
        outputs, feed_dict=dict(zip(inputs, [input_values])))))

make_zip_of_tests(options, test_parameters, build_graph, build_inputs)
