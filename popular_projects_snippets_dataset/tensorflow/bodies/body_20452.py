# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_optimizer.py
"""Compute gradients of "loss" for the variables in "var_list".

    This simply wraps `compute_gradients()` from the real optimizer. The
    gradients will be aggregated in `apply_gradients()` so that user can
    modify the gradients like clipping with per replica global norm if needed.
    The global norm with aggregated gradients can be bad as one replica's huge
    gradients can hurt the gradients from other replicas.

    When the CrossShardOptimizer is constructed with
    `reduction == losses.Reduction.MEAN` (default), this function scales the
    loss by `1.0 / num_shards` before computing the gradients. Assuming the
    optimizer uses the default implementation of `compute_gradients()`, the
    gradients of the scaled loss are scaled by `1.0 / num_shards` compared to
    the gradients of the original loss. This scaling factor is important because
    `apply_gradients()` sums gradients across shards, rather than averaging
    them. However, the scaling factor must be taken into account when clipping
    the norm of the gradients or performing other postprocessing.

    Args:
      loss: A Tensor containing the value to minimize.
      var_list: Optional list or tuple of `tf.Variable` to update to minimize
        `loss`.  Defaults to the list of variables collected in the graph
        under the key `GraphKey.TRAINABLE_VARIABLES`.
      **kwargs: Keyword arguments for compute_gradients().

    Returns:
      A list of (gradient, variable) pairs.

    Raises:
      ValueError: If not within a tpu_shard_context or group_assignment is
        invalid.
    """
num_shards = tpu_function.get_tpu_context().number_of_shards
if num_shards is None:
    logging.warning(
        "CrossShardOptimizer should be used within a tpu_shard_context, but "
        "got unset number_of_shards. Assuming 1.")
    num_shards = 1

subgroup_size = self._verify_and_get_subgroup_size(self._group_assignment,
                                                   num_shards)

if num_shards > 1 and self._reduction == losses.Reduction.MEAN:
    if self._group_assignment:
        scale = 1.0 / subgroup_size
    else:
        scale = 1.0 / num_shards
    loss *= scale

exit(self._opt.compute_gradients(loss, var_list=var_list, **kwargs))
