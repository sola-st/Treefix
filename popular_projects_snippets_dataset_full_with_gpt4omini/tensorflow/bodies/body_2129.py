# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/lstm_test.py
num_inputs = 1
num_nodes = 1
seq_length = 3

weights = array_ops.zeros(lstm.LSTMCellWeightsShape(num_inputs, num_nodes))
m = constant_op.constant([[0.]] * self._batch_size)
c = constant_op.constant([[0.]] * self._batch_size)
x_seq = [constant_op.constant(self._inputs)] * seq_length
pad = constant_op.constant([[0.]] * self._batch_size)

with self.assertRaisesWithPredicateMatch(ValueError, 'length of x_seq'):
    lstm.LSTMLayer('lstm', weights, m, c, x_seq, [pad])
with self.assertRaisesWithPredicateMatch(ValueError, 'length of x_seq'):
    lstm.LSTMLayer('lstm', weights, m, c, x_seq, [pad] * 2)
with self.assertRaisesWithPredicateMatch(ValueError, 'length of x_seq'):
    lstm.LSTMLayer('lstm', weights, m, c, x_seq, [pad] * 4)
