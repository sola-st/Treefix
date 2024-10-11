# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy.py
# TODO(josh11b): In eager mode, use one thread per device.
assert isinstance(var, values.DistributedVariable)
updates = []
for i, v in enumerate(var.values):
    name = "update_%d" % i
    with ops.device(v.device), \
           distribute_lib.UpdateContext(i), \
           ops.name_scope(name):
        # If args and kwargs are not mirrored, the value is returned as is.
        updates.append(
            fn(v, *distribute_utils.select_replica(i, args),
               **distribute_utils.select_replica(i, kwargs)))
exit(distribute_utils.update_regroup(self, updates, group))
