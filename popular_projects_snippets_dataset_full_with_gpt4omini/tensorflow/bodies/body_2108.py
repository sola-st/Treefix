# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/lstm.py
"""Unrolls a single LSTM cell with clipped activations forward by one step.

  Args:
    weights: Weight matrix with shape LSTMCellWeightsShape.
    m_prev: Previous m states with shape [batch_size, num_nodes].
    c_prev: Previous c states with shape [batch_size, num_nodes].
    x: Input with shape [batch_size, num_inputs].
    pad: Padding with shape [batch_size, 1].  Each padding value is either
        0 or 1, where 1 indicates padding; i.e. the input is shorter than the
        sequence length, and the (m, c) states should simply be passed through
        from the previous states.
  Returns:
    The next (m, c) states, each with shape [batch_size, num_nodes].
  """
# Apply weights to the input and previous hidden state.
# The matmul here is the "big" operation.
xm = array_ops.concat([x, m_prev], 1)
xmw = math_ops.matmul(xm, weights)

# Element-wise ops for the standard LSTM cell, with clipped activations.
# XLA can fuse these operations into a single loop.
in_value, in_gate, forget_gate, out_gate = array_ops.split(
    value=xmw, num_or_size_splits=4, axis=1)
in_value = math_ops.tanh(in_value)
in_gate = math_ops.sigmoid(in_gate)
forget_gate = math_ops.sigmoid(forget_gate)
out_gate = math_ops.sigmoid(out_gate)
c_next = Clip(Clip(forget_gate * c_prev) + Clip(in_gate * in_value))
m_next = Clip(out_gate * c_next)

# Account for padding.
c_next = c_prev * pad + c_next * (1.0 - pad)
m_next = m_prev * pad + m_next * (1.0 - pad)

exit((m_next, c_next))
