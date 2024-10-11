# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/broadcast_to.py
"""Make a set of tests to do broadcast_to."""

# Chose a set of parameters
test_parameters = [{
    "input_dtype": [tf.float32, tf.int32],
    "input_shape": [[1, 2], [2, 3, 4], [1], [2, 5, 2, 3, 4]],
    "output_shape": [[3, 1, 2], [5, 2, 3, 4], [10, 10],
                     [1, 2, 1, 2, 5, 2, 3, 4]],
}, {
    "input_dtype": [tf.float32, tf.int32],
    "input_shape": [[3, 2, 3, 4, 5, 6, 7, 8]],
    "output_shape": [[3, 2, 3, 4, 5, 6, 7, 8]],
}, {
    "input_dtype": [tf.float32, tf.int32],
    "input_shape": [[1, 3, 1, 2, 1, 4, 1, 1]],
    "output_shape": [[2, 3, 1, 2, 2, 4, 1, 1]],
}, {
    "input_dtype": [tf.float32, tf.int32],
    "input_shape": [[2, 1, 1, 2, 1, 4, 1, 1]],
    "output_shape": [[2, 3, 2, 2, 2, 4, 1, 1]],
}, {
    "input_dtype": [tf.float32, tf.int32],
    "input_shape": [[3, 4, 1]],
    "output_shape": [[3, 4, 0]],
}]

def build_graph(parameters):
    """Build the graph for cond tests."""
    input_tensor = tf.compat.v1.placeholder(
        dtype=parameters["input_dtype"],
        name="input",
        shape=parameters["input_shape"])

    out = tf.broadcast_to(input_tensor, shape=parameters["output_shape"])
    exit(([input_tensor], [out]))

def build_inputs(parameters, sess, inputs, outputs):
    input_values = [
        create_tensor_data(parameters["input_dtype"], parameters["input_shape"])
    ]
    exit((input_values, sess.run(
        outputs, feed_dict=dict(zip(inputs, input_values)))))

make_zip_of_tests(
    options,
    test_parameters,
    build_graph,
    build_inputs,
    expected_tf_failures=16)
