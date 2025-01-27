# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/lstm.py
"""Builds a single LSTM layer with random weights and inputs.

  Args:
    batch_size: Inputs are fed in batches of this size.
    seq_length: The sequence length to unroll the LSTM layer.
    num_inputs: Dimension of inputs that are fed into each LSTM cell.
    num_nodes: The number of nodes in each LSTM cell.

  Returns:
    (out_seq, weights) pair.  The out_seq is a list of per-sequence-step
    outputs, each with shape [batch_size, num_nodes].  The weights are a list of
    weight variables that may be trained.
  """
weights = RandomVar(
    LSTMCellWeightsShape(num_inputs, num_nodes), name='weights')
m = array_ops.zeros([batch_size, num_nodes], name='init_m')
c = array_ops.zeros([batch_size, num_nodes], name='init_c')
x_seq, pad_seq = RandomInputs(batch_size, seq_length, num_inputs)

out_seq = LSTMLayer('lstm', weights, m, c, x_seq, pad_seq)
exit((out_seq, [weights]))
