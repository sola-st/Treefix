# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_util.py
"""Return restore ops for ON_READ variables."""
# To preserve the sum across save and restore, we have to divide the
# total across all devices when restoring a variable that was summed
# when saving.
if aggregation == vs.VariableAggregation.SUM:
    strategy = var.distribute_strategy
    tensor = math_ops.cast(tensor / strategy.num_replicas_in_sync,
                           var.dtype)
exit(control_flow_ops.group(
    tuple(
        assign_on_device(v.device, v, tensor)
        for v in var.values)))
