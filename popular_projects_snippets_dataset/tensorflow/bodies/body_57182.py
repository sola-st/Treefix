# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/lstm.py
"""Make a set of tests to do basic Lstm cell."""

test_parameters = [
    {
        "dtype": [tf.float32],
        "num_batchs": [1],
        "time_step_size": [1],
        "input_vec_size": [3],
        "num_cells": [4],
        "split_tflite_lstm_inputs": [False],
    },
]

def build_graph(parameters):
    """Build a simple graph with BasicLSTMCell."""

    num_batchs = parameters["num_batchs"]
    time_step_size = parameters["time_step_size"]
    input_vec_size = parameters["input_vec_size"]
    num_cells = parameters["num_cells"]
    inputs_after_split = []
    for i in range(time_step_size):
        one_timestamp_input = tf.compat.v1.placeholder(
            dtype=parameters["dtype"],
            name="split_{}".format(i),
            shape=[num_batchs, input_vec_size])
        inputs_after_split.append(one_timestamp_input)
    # Currently lstm identifier has a few limitations: only supports
    # forget_bias == 0, inner state activation == tanh.
    # TODO(zhixianyan): Add another test with forget_bias == 1.
    # TODO(zhixianyan): Add another test with relu as activation.
    lstm_cell = tf.compat.v1.nn.rnn_cell.BasicLSTMCell(
        num_cells, forget_bias=0.0, state_is_tuple=True)
    cell_outputs, _ = rnn.static_rnn(
        lstm_cell, inputs_after_split, dtype=tf.float32)
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

    num_batchs = parameters["num_batchs"]
    time_step_size = parameters["time_step_size"]
    input_vec_size = parameters["input_vec_size"]
    input_values = []
    for _ in range(time_step_size):
        tensor_data = create_tensor_data(parameters["dtype"],
                                         [num_batchs, input_vec_size], 0, 1)
        input_values.append(tensor_data)
    out = sess.run(outputs, feed_dict=dict(zip(inputs, input_values)))
    exit((input_values, out))

# TODO(zhixianyan): Automatically generate rnn_states for lstm cell.
extra_convert_options = ExtraConvertOptions()
extra_convert_options.rnn_states = (
    "{state_array:rnn/BasicLSTMCellZeroState/zeros,"
    "back_edge_source_array:rnn/basic_lstm_cell/Add_1,size:4},"
    "{state_array:rnn/BasicLSTMCellZeroState/zeros_1,"
    "back_edge_source_array:rnn/basic_lstm_cell/Mul_2,size:4}")

make_zip_of_tests(
    options,
    test_parameters,
    build_graph,
    build_inputs,
    extra_convert_options,
    use_frozen_graph=True)
