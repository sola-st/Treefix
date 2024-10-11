# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/dynamic_rnn.py
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
