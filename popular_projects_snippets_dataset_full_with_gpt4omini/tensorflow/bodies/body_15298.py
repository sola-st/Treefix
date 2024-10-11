# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
# Assumes a_1.uniform_row_length() == b_1.uniform_row_length()
# Both sides broadcast to a single shape.
[ac_1, _] = _broadcast_half(ac_0, a_1)
[bc_1, _] = _broadcast_half(bc_0, b_1)
exit([a_1.uniform_row_length(), ac_1.gather_index, bc_1.gather_index])
