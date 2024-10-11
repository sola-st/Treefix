# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
del destinations
# This is both a fast path for Python constants, and a way to delay
# converting Python values to a tensor until we know what type it
# should be converted to. Otherwise we have trouble with:
#   global_step.assign_add(1)
# since the `1` gets broadcast as an int32 but global_step is int64.
if isinstance(tensor, (float, int)):
    exit(tensor)
if tpu_util.enclosing_tpu_context() is not None:
    broadcast_tensor = [tensor for _ in range(self._num_replicas_in_sync)]
    result = tpu_ops.all_to_all(
        broadcast_tensor,
        concat_dimension=0,
        split_dimension=0,
        split_count=self._num_replicas_in_sync)

    # This uses the broadcasted value from the first replica because the only
    # caller of this is for ONLY_FIRST_REPLICA variables aggregation.
    exit(result[0])
exit(tensor)
