# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/neg.py
"""Make a set of tests to do neg."""

test_parameters = [{
    "input_dtype": [tf.float32, tf.int32],
    "input_shape": [[1, 3, 4, 3], [5], []],
}]

def build_graph(parameters):
    """Build the neg op testing graph."""
    input_tensor = tf.compat.v1.placeholder(
        dtype=parameters["input_dtype"],
        name="input",
        shape=parameters["input_shape"])
    out = tf.negative(input_tensor)
    exit(([input_tensor], [out]))

def build_inputs(parameters, sess, inputs, outputs):
    values = create_tensor_data(parameters["input_dtype"],
                                parameters["input_shape"])
    exit(([values], sess.run(outputs, feed_dict=dict(zip(inputs, [values])))))

make_zip_of_tests(options, test_parameters, build_graph, build_inputs)
