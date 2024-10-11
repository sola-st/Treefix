# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy.py
if self._use_merge_call():
    exit(super()._replica_ctx_update(var, fn, args, kwargs, group))

replica_context = distribution_strategy_context.get_replica_context()
assert replica_context
replica_id = values_util.get_current_replica_id_as_int()
name = "update_%d" % replica_id

if isinstance(var, values.DistributedVariable):
    var = var._get_replica(replica_id)  # pylint: disable=protected-access

with ops.device(var.device), ops.name_scope(name):
    result = fn(var, *args, **kwargs)
exit(result)
