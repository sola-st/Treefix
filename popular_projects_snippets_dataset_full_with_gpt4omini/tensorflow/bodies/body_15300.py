# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
[ac_1, c_1a] = _broadcast_half(ac_0, a_1)
bc_1_gather_index = array_ops.gather(bc_0.gather_index, c_1a.value_rowids())
exit([a_1.uniform_row_length(), ac_1.gather_index, bc_1_gather_index])
