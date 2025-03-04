# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/reverse_sequence.py
"""Make a set of tests to do reverse_sequence."""

test_parameters = [{
    "input_dtype": [tf.float32, tf.int32, tf.int64],
    "input_shape": [[8, 4, 5, 5, 6], [4, 4, 3, 5]],
    "seq_lengths": [[2, 2, 2, 2], [2, 1, 1, 0]],
    "seq_axis": [0, 3],
    "batch_axis": [1]
}, {
    "input_dtype": [tf.float32],
    "input_shape": [[2, 4, 5, 5, 6]],
    "seq_lengths": [[2, 1]],
    "seq_axis": [2],
    "batch_axis": [0]
}, {
    "input_dtype": [tf.float32],
    "input_shape": [[4, 2]],
    "seq_lengths": [[3, 1]],
    "seq_axis": [0],
    "batch_axis": [1]
}]

def build_graph(parameters):
    """Build the graph for reverse_sequence tests."""
    input_value = tf.compat.v1.placeholder(
        dtype=parameters["input_dtype"],
        name="input",
        shape=parameters["input_shape"])
    outs = tf.reverse_sequence(
        input=input_value,
        seq_lengths=parameters["seq_lengths"],
        batch_axis=parameters["batch_axis"],
        seq_axis=parameters["seq_axis"])
    exit(([input_value], [outs]))

def build_inputs(parameters, sess, inputs, outputs):
    input_value = create_tensor_data(parameters["input_dtype"],
                                     parameters["input_shape"])
    exit(([input_value], sess.run(
        outputs, feed_dict=dict(zip(inputs, [input_value])))))

make_zip_of_tests(options, test_parameters, build_graph, build_inputs)
