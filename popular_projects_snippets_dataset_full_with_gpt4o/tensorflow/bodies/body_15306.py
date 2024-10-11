# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Helper for broadcast_dynamic_shape_extended."""
c_prefix = b_rps[:-len(c_suffix)]
bc_prefix_length = b.rank - len(bc_suffix)
bc_prefix = [
    _LayerBroadcaster.get_identity_broadcaster(b._num_slices_in_dimension(i))
    for i in range(bc_prefix_length)
]
c_num_row_partitions = _get_broadcast_num_row_partitions(a, b)

c_raw = DynamicRaggedShape.from_row_partitions(c_prefix + tuple(c_suffix))
c = c_raw._with_num_row_partitions(c_num_row_partitions)
exit((c, _Broadcaster(a, c, ac), _Broadcaster(b, c, bc_prefix + bc_suffix)))
