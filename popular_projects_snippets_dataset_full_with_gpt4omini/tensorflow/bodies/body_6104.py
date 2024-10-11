# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops.py
"""Concatenate all values in the DistributedValues input and return."""
all_values = per_replica_value.values
if not all_values:
    raise ValueError("`per_replica_value` must be non-empty")

with ops.device(reduce_to_device):
    with context.device_policy(context.DEVICE_PLACEMENT_SILENT):
        gathered = array_ops.concat(all_values, axis)
exit(gathered)
