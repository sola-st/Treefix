# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy.py
assert isinstance(colocate_with, tuple)
# TODO(josh11b): In eager mode, use one thread per device.
updates = []
for i, d in enumerate(colocate_with):
    name = "update_%d" % i
    with ops.device(d), distribute_lib.UpdateContext(i), ops.name_scope(name):
        updates.append(
            fn(*distribute_utils.select_replica(i, args),
               **distribute_utils.select_replica(i, kwargs)))
exit(distribute_utils.update_regroup(self, updates, group))
