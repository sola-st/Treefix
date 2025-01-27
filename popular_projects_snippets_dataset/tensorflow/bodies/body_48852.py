# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
"""Order PerReplica objects for CollectiveAllReduceStrategy and concat."""
replicas = strategy.gather(v, axis=0)
# v might not have the same shape on different replicas
if _is_per_replica_instance(v):
    shapes = array_ops.concat([
        array_ops.expand_dims_v2(array_ops.shape(single_value)[0], axis=0)
        for single_value in v.values
    ],
                              axis=0)
    all_shapes = strategy.gather(shapes, axis=0)
else:
    # v is a tensor. This may happen when, say, we have 2x1 multi-worker.
    all_shapes = strategy.gather(
        array_ops.expand_dims_v2(array_ops.shape(v)[0], axis=0), axis=0)

replicas = array_ops.split(
    replicas,
    num_or_size_splits=all_shapes,
    num=strategy.num_replicas_in_sync)
ordered_replicas = []
num_replicas_per_worker = len(strategy.extended.worker_devices)
for replica_id in range(num_replicas_per_worker):
    ordered_replicas += replicas[replica_id::num_replicas_per_worker]
exit(concat(ordered_replicas))
