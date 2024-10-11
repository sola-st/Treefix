# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/softmax.py
"""Make a set of tests to do softmax."""

test_parameters = [{
    "dtype": [tf.float32],
    "input_shape": [[1, 3, 4, 3], [2, 3], [3], [1, 4], [1, 1, 5],
                    [1, 1, 1, 6]],
    "dim": [-1, 0],
    "fully_quantize": [False, True],
}, {
    "dtype": [tf.float32],
    "input_shape": [[4, 7]],
    "dim": [-1, 1],
    "fully_quantize": [False, True],
}]

def build_graph(parameters):
    input_tensor = tf.compat.v1.placeholder(
        dtype=parameters["dtype"],
        name="input",
        shape=parameters["input_shape"])
    out = tf.nn.softmax(input_tensor, axis=parameters["dim"])
    exit(([input_tensor], [out]))

def build_inputs(parameters, sess, inputs, outputs):
    input_values = create_tensor_data(
        parameters["dtype"],
        parameters["input_shape"],
        min_value=-1,
        max_value=1)
    exit(([input_values], sess.run(
        outputs, feed_dict=dict(zip(inputs, [input_values])))))

make_zip_of_tests(options, test_parameters, build_graph, build_inputs)
