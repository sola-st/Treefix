# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/space_to_depth.py
"""Make a set of tests to do space_to_depth."""

test_parameters = [{
    "dtype": [tf.float32, tf.int32, tf.uint8, tf.int64],
    "input_shape": [[2, 12, 24, 1]],
    "block_size": [2, 3, 4],
    "fully_quantize": [False],
}, {
    "dtype": [tf.float32],
    "input_shape": [[2, 12, 24, 1], [1, 12, 24, 1]],
    "block_size": [2, 3, 4],
    "fully_quantize": [True],
}]

def build_graph(parameters):
    input_tensor = tf.compat.v1.placeholder(
        dtype=parameters["dtype"],
        name="input",
        shape=parameters["input_shape"])
    out = tf.compat.v1.space_to_depth(
        input=input_tensor, block_size=parameters["block_size"])
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
