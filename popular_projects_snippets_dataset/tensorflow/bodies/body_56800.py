# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/depth_to_space.py
"""Make a set of tests to do depth_to_space."""

test_parameters = [{
    "dtype": [tf.int32, tf.uint8, tf.int64],
    "input_shape": [[2, 3, 4, 16]],
    "block_size": [2, 4],
    "fully_quantize": [False],
}, {
    "dtype": [tf.float32],
    "input_shape": [[2, 3, 4, 16]],
    "block_size": [2, 4],
    "fully_quantize": [True, False],
}]

def build_graph(parameters):
    input_tensor = tf.compat.v1.placeholder(
        dtype=parameters["dtype"],
        name="input",
        shape=parameters["input_shape"])
    out = tf.compat.v1.depth_to_space(
        input_tensor, block_size=parameters["block_size"])
    exit(([input_tensor], [out]))

def build_inputs(parameters, sess, inputs, outputs):
    if not parameters["fully_quantize"]:
        input_values = create_tensor_data(parameters["dtype"],
                                          parameters["input_shape"])
    else:
        input_values = create_tensor_data(
            parameters["dtype"],
            parameters["input_shape"],
            min_value=-1,
            max_value=1)
    exit(([input_values], sess.run(
        outputs, feed_dict=dict(zip(inputs, [input_values])))))

make_zip_of_tests(options, test_parameters, build_graph, build_inputs)
