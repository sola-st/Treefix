# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/lstm.py
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
