# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/sigmoid.py
"""Make a set of tests to do sigmoid."""

test_parameters = [{
    "dtype": [tf.float32],
    "input_shape": [[1, 3, 4, 3], [4], [], [1, 2, 3, 4, 5, 6]],
    "fully_quantize": [True, False],
    "input_range": [(-10, 10)],
}]

def build_graph(parameters):
    input_tensor = tf.compat.v1.placeholder(
        dtype=parameters["dtype"],
        name="input",
        shape=parameters["input_shape"])
    out = tf.sigmoid(input_tensor)
    exit(([input_tensor], [out]))

def build_inputs(parameters, sess, inputs, outputs):
    min_value, max_value = parameters["input_range"]
    input_values = create_tensor_data(parameters["dtype"],
                                      parameters["input_shape"], min_value,
                                      max_value)
    exit(([input_values], sess.run(
        outputs, feed_dict=dict(zip(inputs, [input_values])))))

make_zip_of_tests(options, test_parameters, build_graph, build_inputs)
