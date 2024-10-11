# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/unfused_gru.py
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
