# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/unique.py
"""Make a set of tests for Unique op."""

test_parameters = [{
    "input_shape": [[1]],
    "index_type": [tf.int32, tf.int64, None],
    "input_values": [3]
}, {
    "input_shape": [[5]],
    "index_type": [tf.int32, tf.int64],
    "input_values": [[3, 2, 1, 2, 3]]
}, {
    "input_shape": [[7]],
    "index_type": [tf.int32, tf.int64],
    "input_values": [[1, 1, 1, 1, 1, 1, 1]]
}, {
    "input_shape": [[5]],
    "index_type": [tf.int32, tf.int64],
    "input_values": [[3, 2, 1, 0, -1]]
}]

def build_graph(parameters):
    """Build the graph for the test case."""

    input_tensor = tf.compat.v1.placeholder(
        dtype=tf.int32, name="input", shape=parameters["input_shape"])
    if parameters["index_type"] is None:
        output = tf.unique(input_tensor)
    else:
        output = tf.unique(input_tensor, parameters["index_type"])

    exit(([input_tensor], output))

def build_inputs(parameters, sess, inputs, outputs):
    input_values = [create_tensor_data(tf.int32, parameters["input_shape"])]
    exit((input_values, sess.run(
        outputs, feed_dict=dict(zip(inputs, input_values)))))

make_zip_of_tests(options, test_parameters, build_graph, build_inputs)
