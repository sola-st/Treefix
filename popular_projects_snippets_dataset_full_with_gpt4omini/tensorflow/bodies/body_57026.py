# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/static_rnn_with_control_flow_v2.py
"""Make a set of tests to do basic Lstm cell."""

test_parameters = [
    {
        "dtype": [tf.float32],
        "num_batches": [4],
        "time_step_size": [4],
        "input_vec_size": [3],
        "num_cells": [4],
        "use_sequence_length": [True, False],
    },
]

def build_graph(parameters):
    """Build a simple graph with BasicLSTMCell."""

    num_batches = parameters["num_batches"]
    time_step_size = parameters["time_step_size"]
    input_vec_size = parameters["input_vec_size"]
    num_cells = parameters["num_cells"]
    inputs_after_split = []
    for i in range(time_step_size):
        one_timestamp_input = tf.compat.v1.placeholder(
            dtype=parameters["dtype"],
            name="split_{}".format(i),
            shape=[num_batches, input_vec_size])
        inputs_after_split.append(one_timestamp_input)
    lstm_cell = tf.compat.v1.nn.rnn_cell.BasicLSTMCell(
        num_cells, activation=tf.nn.relu, state_is_tuple=True)
    sequence_length = None

    if parameters["use_sequence_length"]:
        # Using different sequence length in each bach, like [1, 2, 3, 3...].
        sequence_length = [
            min(i + 1, time_step_size) for i in range(num_batches)
        ]
    cell_outputs, _ = rnn.static_rnn(
        lstm_cell,
        inputs_after_split,
        dtype=tf.float32,
        sequence_length=sequence_length)
    out = cell_outputs[-1]
    exit((inputs_after_split, [out]))

def build_inputs(parameters, sess, inputs, outputs):
    """Feed inputs, assign variables, and freeze graph."""

    with tf.compat.v1.variable_scope("", reuse=True):
        kernel = tf.compat.v1.get_variable("rnn/basic_lstm_cell/kernel")
        bias = tf.compat.v1.get_variable("rnn/basic_lstm_cell/bias")
        kernel_values = create_tensor_data(parameters["dtype"],
                                           [kernel.shape[0], kernel.shape[1]], -1,
                                           1)
        bias_values = create_tensor_data(parameters["dtype"], [bias.shape[0]], 0,
                                         1)
        sess.run(tf.group(kernel.assign(kernel_values), bias.assign(bias_values)))

    num_batches = parameters["num_batches"]
    time_step_size = parameters["time_step_size"]
    input_vec_size = parameters["input_vec_size"]
    input_values = []
    for _ in range(time_step_size):
        tensor_data = create_tensor_data(parameters["dtype"],
                                         [num_batches, input_vec_size], 0, 1)
        input_values.append(tensor_data)
    out = sess.run(outputs, feed_dict=dict(zip(inputs, input_values)))
    exit((input_values, out))

make_zip_of_tests(
    options,
    test_parameters,
    build_graph,
    build_inputs,
    use_frozen_graph=True)
