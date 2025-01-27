# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/exp.py
"""Make a set of tests to do exp."""

test_parameters = [{
    "input_dtype": [tf.float32],
    "input_shape": [[], [3], [1, 100], [4, 2, 3], [5, 224, 224, 3]],
}]

def build_graph(parameters):
    """Build the exp op testing graph."""
    input_tensor = tf.compat.v1.placeholder(
        dtype=parameters["input_dtype"],
        name="input",
        shape=parameters["input_shape"])

    out = tf.exp(input_tensor)
    exit(([input_tensor], [out]))

def build_inputs(parameters, sess, inputs, outputs):
    values = [
        create_tensor_data(
            parameters["input_dtype"],
            parameters["input_shape"],
            min_value=-100,
            max_value=9)
    ]
    exit((values, sess.run(outputs, feed_dict=dict(zip(inputs, values)))))

make_zip_of_tests(options, test_parameters, build_graph, build_inputs)
