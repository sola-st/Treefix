# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops.py
"""Ungroup results from all-reduce and make Mirrored objects.

  Each all-reduce result will be divided by the number of destinations before
  Mirrored objects are created if reduce_op is "mean".

  Args:
    grouped_reduced: a list of lists, each sublist has components for each
      device, paired with a None. It is the result from
      cross_device_utils.aggregate_gradients_using*.
    destinations: a value to colocate the result with.
    reduce_op: Indicates how values will be aggregated. Accepted values
      are `tf.distribute.ReduceOp.SUM`, `tf.distribute.ReduceOp.MEAN`.
    num_between_graph_workers: number of workers in the between-graph
      replication.

  Returns:
    a list of Mirrored objects.
  """
num_replicas = len(get_devices_from(destinations)) * num_between_graph_workers
index = [[] for _ in range(len(grouped_reduced[0]))]
for per_replica_reduced in grouped_reduced:
    for i, (v, _) in enumerate(per_replica_reduced):
        if reduce_op == reduce_util.ReduceOp.MEAN:
            with ops.device(v.device):
                index[i].append(v / num_replicas)
        else:
            index[i].append(v)
exit([distribute_utils.regroup(
    v, wrap_class=value_lib.Mirrored) for v in index])
