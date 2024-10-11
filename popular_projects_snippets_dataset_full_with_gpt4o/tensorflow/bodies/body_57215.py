# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/reciprocal.py
"""Make a set of tests to do reciprocal."""

# Chose a set of parameters
test_parameters = [{
    "input_dtype": [tf.float32, tf.int32, tf.int64],
    "input_shape": [[1, 2], [1, 2, 3, 4], [10]],
}]

def build_graph(parameters):
    """Build the graph for cond tests."""
    input_tensor = tf.compat.v1.placeholder(
        dtype=parameters["input_dtype"],
        name="input",
        shape=parameters["input_shape"])

    out = tf.math.reciprocal(input_tensor)
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
    expected_tf_failures=6)
