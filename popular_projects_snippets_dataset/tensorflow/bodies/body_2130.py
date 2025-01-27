# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/lstm_test.py
with self.session() as sess:
    num_inputs = 1
    num_nodes = 1
    seq_length = 3

    weights = init_weights(lstm.LSTMCellWeightsShape(num_inputs, num_nodes))
    m_init = constant_op.constant([[m_init_scalar]] * self._batch_size)
    c_init = constant_op.constant([[c_init_scalar]] * self._batch_size)
    x_seq = [constant_op.constant(self._inputs)] * seq_length
    pad_seq = [constant_op.constant([[pad_scalar]] * self._batch_size)
              ] * seq_length

    out_seq = lstm.LSTMLayer('lstm', weights, m_init, c_init, x_seq, pad_seq)
    _DumpGraph(sess.graph, 'lstm_layer_%s_%d_%d_%d' %
               (basename, m_init_scalar, c_init_scalar, pad_scalar))

    # Initialize variables and run the unrolled LSTM layer.
    self.evaluate(variables.global_variables_initializer())
    exit(self.evaluate(out_seq))
