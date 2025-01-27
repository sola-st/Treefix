# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_optimizer.py
"""Construct a new cross-shard optimizer.

    Args:
      opt: An existing `Optimizer` to encapsulate.
      reduction: The reduction to apply to the shard losses.
      name: Optional name prefix for the operations created when applying
        gradients. Defaults to "CrossShardOptimizer".
      group_assignment: Optional 2d int32 lists with shape
        [num_groups, num_replicas_per_group] which describles how to apply
        optimizer to subgroups.

    Raises:
      ValueError: If reduction is not a valid cross-shard reduction.
    """
accepted_reductions = (losses.Reduction.SUM, losses.Reduction.MEAN)
if reduction not in accepted_reductions:
    raise ValueError(
        f"Argument `reduction` should be one of {accepted_reductions}. "
        f"Received: {reduction}")
if not isinstance(opt, optimizer.Optimizer):
    raise TypeError(
        "CrossShardOptimizer only works with tf.training.Optimizer and not "
        f"Keras Optimizer. Received: {opt}. "
        "If you are using TPUStrategy, "
        "Keras Optimizer will sum gradients across replicas."
        "If you are using TPUEstimator, you may instead sum your gradients "
        "with:\n"
        "`grads = [tf.compat.v1.tpu.cross_replica_sum(g) for g in grads]`\n"
        "If you want to average your gradients, rescale your loss with: "
        "`loss /= global_batch_size`")

super(CrossShardOptimizer, self).__init__(False, name)
self._opt = opt
self._reduction = reduction
self._group_assignment = group_assignment
