# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/log_softmax.py
"""Make a set of tests to do log_softmax."""

test_parameters = [{
    "input_dtype": [tf.float32],
    "input_shape": [[1, 100], [4, 2], [5, 224]],
}]

def build_graph(parameters):
    """Build the log_softmax op testing graph."""
    input_tensor = tf.compat.v1.placeholder(
        dtype=parameters["input_dtype"],
        name="input",
        shape=parameters["input_shape"])

    out = tf.nn.log_softmax(input_tensor)
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
