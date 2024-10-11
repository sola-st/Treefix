# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/unfused_gru.py
"""Make a set of tests for unfused gru op."""

test_parameters = [{
    "units": [2, 5],
    "batch_size": [1, 2],
    "time": [3],
}]

def build_graph(parameters):
    """Build the graph for unfused_gru."""
    inputs = [
        tf.compat.v1.placeholder(
            tf.float32, [parameters["batch_size"], parameters["units"]])
        for _ in range(parameters["time"])
    ]
    cell_fw = tf.compat.v1.nn.rnn_cell.GRUCell(parameters["units"])
    cell_bw = tf.compat.v1.nn.rnn_cell.GRUCell(parameters["units"])
    outputs, _, _ = tf.compat.v1.nn.static_bidirectional_rnn(
        cell_fw, cell_bw, inputs, dtype=tf.float32)

    exit((inputs, outputs))

def build_inputs(parameters, sess, inputs, outputs):
    """Build the inputs for unfused_gru."""
    input_values = [
        create_tensor_data(tf.float32,
                           [parameters["batch_size"], parameters["units"]])
        for _ in range(parameters["time"])
    ]
    init = tf.compat.v1.global_variables_initializer()
    sess.run(init)
    exit((input_values, sess.run(
        outputs, feed_dict=dict(zip(inputs, input_values)))))

make_zip_of_tests(
    options,
    test_parameters,
    build_graph,
    build_inputs,
    use_frozen_graph=True)
