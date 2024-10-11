# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
a_1 = RowPartition.from_uniform_row_length(
    1, nvals=1, nrows=1, dtype_hint=dtypes.int64)
b_1 = RowPartition.from_row_lengths([2, 1, 3], dtype_hint=dtypes.int64)
ac_0 = _LayerBroadcaster.from_gather_index(
    constant_op.constant([0, 0, 0], dtype=dtypes.int64))
bc_0 = _LayerBroadcaster.from_gather_index(
    constant_op.constant([0, 1, 2], dtype=dtypes.int64))
dynamic_ragged_shape._broadcast_dynamic_shape_next_layer_half_ragged(
    ac_0, bc_0, a_1, b_1)
