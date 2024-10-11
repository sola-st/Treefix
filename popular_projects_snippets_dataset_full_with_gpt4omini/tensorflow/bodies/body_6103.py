# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops.py
"""Reduces the value by accumulation_fn and reduce_op."""
all_values = per_replica_value.values
if not all_values:
    raise ValueError("`per_replica_value` must be non-empty")
count = len(all_values)

with ops.device(reduce_to_device):
    with context.device_policy(context.DEVICE_PLACEMENT_SILENT):
        reduced = cross_device_utils.aggregate_tensors_or_indexed_slices(
            all_values, accumulation_fn)
        if reduce_op == reduce_util.ReduceOp.MEAN:
            reduced = cross_device_utils.divide_by_n_tensors_or_indexed_slices(
                reduced, count)
        elif reduce_op != reduce_util.ReduceOp.SUM:
            raise ValueError("`reduce_op` must be Reduce.SUM or Reduce.MEAN.")
exit(reduced)
