# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/static_rnn_with_control_flow_v2.py
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
