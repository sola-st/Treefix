# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/abs.py
"""Make a set of tests to do abs."""

# Chose a set of parameters
test_parameters = [{
    "input_shape": [[], [1], [2, 3], [1, 1, 1, 1], [1, 3, 4, 3],
                    [3, 15, 14, 3], [3, 1, 2, 4, 6], [2, 2, 3, 4, 5, 6]],
    "dtype": [tf.float32],
    "dynamic_range_quantize": [False, True],
    "fully_quantize": [False],
    "input_range": [(-10, 10), (-10, 0)],
}, {
    "input_shape": [[], [1], [2, 3], [1, 1, 1, 1], [1, 3, 4, 3],
                    [3, 15, 14, 3], [3, 1, 2, 4, 6], [2, 2, 3, 4, 5, 6]],
    "dtype": [tf.float32],
    "dynamic_range_quantize": [False],
    "fully_quantize": [True],
    "input_range": [(-10, 10)],
}, {
    "input_shape": [[], [1], [2, 3], [1, 1, 1, 1],
                    [1, 3, 4, 3], [3, 15, 14, 3],
                    [3, 1, 2, 4, 6], [2, 2, 3, 4, 5, 6]],
    "dtype": [tf.int16],
}]

def build_graph(parameters):
    input_tensor = tf.compat.v1.placeholder(
        dtype=parameters["dtype"],
        name="input",
        shape=parameters["input_shape"])
    out = tf.abs(input_tensor)
    exit(([input_tensor], [out]))

def build_inputs(parameters, sess, inputs, outputs):
    min_value, max_value = (-10, 10)
    if "input_range" in parameters:
        min_value, max_value = parameters["input_range"]
    input_values = create_tensor_data(
        parameters["dtype"],
        parameters["input_shape"],
        min_value=min_value,
        max_value=max_value)
    exit(([input_values], sess.run(
        outputs, feed_dict=dict(zip(inputs, [input_values])))))

make_zip_of_tests(options, test_parameters, build_graph, build_inputs)
