# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/cos.py
"""Make a set of tests to do cos."""

test_parameters = [{
    "input_dtype": [tf.float32],
    "input_shape": [[], [3], [1, 100], [4, 2, 3], [5, 224, 224, 3]],
}]

def build_graph(parameters):
    """Build the cos op testing graph."""
    input_tensor = tf.compat.v1.placeholder(
        dtype=parameters["input_dtype"],
        name="input",
        shape=parameters["input_shape"])

    out = tf.cos(input_tensor)
    exit(([input_tensor], [out]))

def build_inputs(parameters, sess, inputs, outputs):
    values = [
        create_tensor_data(
            parameters["input_dtype"],
            parameters["input_shape"],
            min_value=-np.pi,
            max_value=np.pi)
    ]
    exit((values, sess.run(outputs, feed_dict=dict(zip(inputs, values)))))

make_zip_of_tests(options, test_parameters, build_graph, build_inputs)
