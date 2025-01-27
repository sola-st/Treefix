# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/lstm_test.py
with self.session() as sess:
    num_inputs = 1
    num_nodes = 1

    weights = init_weights(lstm.LSTMCellWeightsShape(num_inputs, num_nodes))
    m_prev = constant_op.constant([[m_prev_scalar]] * self._batch_size)
    c_prev = constant_op.constant([[c_prev_scalar]] * self._batch_size)
    x = constant_op.constant(self._inputs)
    pad = constant_op.constant([[pad_scalar]] * self._batch_size)

    m, c = lstm.LSTMCell(weights, m_prev, c_prev, x, pad)
    _DumpGraph(sess.graph, 'lstm_cell_%s_%d_%d_%d' %
               (basename, m_prev_scalar, c_prev_scalar, pad_scalar))

    # Initialize variables and run the unrolled LSTM step.
    self.evaluate(variables.global_variables_initializer())
    exit(self.evaluate([m, c]))
