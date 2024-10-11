# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/relu6.py
"""Make a set of tests to do relu6."""

# Chose a set of parameters
test_parameters = [{
    "input_shape": [[], [1, 1, 1, 1], [1, 3, 4, 3], [3, 15, 14, 3],
                    [3, 1, 2, 4, 6], [2, 2, 3, 4, 5, 6]],
    "fully_quantize": [True, False],
    "input_range": [(-2, 8)]
}]

def build_graph(parameters):
    input_tensor = tf.compat.v1.placeholder(
        dtype=tf.float32, name="input", shape=parameters["input_shape"])
    out = tf.nn.relu6(input_tensor)
    exit(([input_tensor], [out]))

def build_inputs(parameters, sess, inputs, outputs):
    min_value, max_value = parameters["input_range"]
    input_values = create_tensor_data(np.float32, parameters["input_shape"],
                                      min_value, max_value)
    exit(([input_values], sess.run(
        outputs, feed_dict=dict(zip(inputs, [input_values])))))

make_zip_of_tests(options, test_parameters, build_graph, build_inputs)
