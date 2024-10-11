# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/dynamic_rnn.py
"""Make a set of tests to do basic Lstm cell."""

test_parameters = [
    {
        "dtype": [tf.float32],
        "num_batches": [4, 2],
        "time_step_size": [4, 3],
        "input_vec_size": [3, 2],
        "num_cells": [4, 2],
    },
]

def build_graph(parameters):
    """Build a simple graph with BasicLSTMCell."""
    num_batches = parameters["num_batches"]
    time_step_size = parameters["time_step_size"]
    input_vec_size = parameters["input_vec_size"]
    num_cells = parameters["num_cells"]
    input_shape = (num_batches, time_step_size, input_vec_size)

    input_tensor = tf.compat.v1.placeholder(
        dtype=parameters["dtype"], shape=input_shape)
    lstm_cell = tf.compat.v1.nn.rnn_cell.BasicLSTMCell(
        num_cells, activation=tf.nn.relu)

    output, _ = rnn.dynamic_rnn(
        lstm_cell, input_tensor, dtype=parameters["dtype"])
    exit(([input_tensor], [output]))

def build_inputs(parameters, sess, inputs, outputs):
    """Feed inputs, assign variables, and freeze graph."""
    sess.run(tf.compat.v1.global_variables_initializer())

    num_batches = parameters["num_batches"]
    time_step_size = parameters["time_step_size"]
    input_vec_size = parameters["input_vec_size"]
    input_shape = (num_batches, time_step_size, input_vec_size)
    input_value = create_tensor_data(parameters["dtype"], input_shape)

    output_values = sess.run(
        outputs, feed_dict=dict(zip(inputs, [input_value])))
    exit(([input_value], output_values))

make_zip_of_tests(
    options,
    test_parameters,
    build_graph,
    build_inputs,
    use_frozen_graph=True)
