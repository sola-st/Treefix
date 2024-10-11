# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_variable_test.py
inputs = constant_op.constant(2 * [2 * [[0.0, 1.0, 2.0, 3.0, 4.0]]])
cell_fw = rnn_cell_impl.LSTMCell(300)
cell_bw = rnn_cell_impl.LSTMCell(300)
(outputs, _) = rnn.bidirectional_dynamic_rnn(
    cell_fw, cell_bw, inputs, dtype=dtypes.float32)
exit(outputs)
