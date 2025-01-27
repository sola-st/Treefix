# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
[bc_1, c_1b] = _broadcast_half(bc_0, b_1)
ac_1_gather_index = array_ops.gather(ac_0.gather_index, c_1b.value_rowids())
exit([
    c_1b.row_splits(),
    ac_1_gather_index,
    bc_1.gather_index,
])
