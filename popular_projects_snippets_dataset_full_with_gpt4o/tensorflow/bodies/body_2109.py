# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/lstm.py
"""Unrolls a layer of LSTM cells forward by the sequence length.

  The sequence length is determined by the length of x_seq and pad_seq, which
  must be the same.

  Args:
    cell_name: Base name of each cell.
    weights: Weight matrix with shape LSTMCellWeightsShape.
    m: Initial m states with shape [batch_size, num_nodes].
    c: Initial c states with shape [batch_size, num_nodes].
    x_seq: List of inputs, each with shape [batch_size, num_inputs].
        The length of the list is the sequence length.
    pad_seq: List of paddings, each with shape [batch_size, 1].
        The length of the list is the sequence length.
        Each padding value is either 0 or 1, where 1 indicates padding;
        i.e. the input is shorter than the sequence length.
  Returns:
    List of per-sequence-step outputs, each with shape [batch_size, num_nodes].
  Raises:
    ValueError: If len(x_seq) != len(pad_seq).
  """
if len(x_seq) != len(pad_seq):
    raise ValueError('length of x_seq(%d) != pad_seq(%d)' %
                     (len(x_seq), len(pad_seq)))
out_seq = []
for seq in range(len(x_seq)):
    with ops.name_scope('%s_%d' % (cell_name, seq)):
        m, c = LSTMCell(weights, m, c, x_seq[seq], pad_seq[seq])
        out_seq.append(array_ops.identity(m, name='out'))
exit(out_seq)
