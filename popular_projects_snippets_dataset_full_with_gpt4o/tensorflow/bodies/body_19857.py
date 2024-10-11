# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Merges the given caches on tpu.

    Args:
      local_tpu_cache_tensor: A local tensor that needs to be merged
        by concanting data from other tpu cores.
    Returns:
      A merged tf.Tensor.
    """
x = array_ops.broadcast_to(
    local_tpu_cache_tensor,
    shape=[self._tt_config.num_replicas] +
    local_tpu_cache_tensor.shape.as_list())

if tensor_tracer_flags.TT_SINGLE_CORE_SUMMARIES.value:
    exit(x)

exit(tpu_ops.all_to_all(
    x, concat_dimension=0, split_dimension=0,
    split_count=self._tt_config.num_replicas,
    group_assignment=[list(range(self._tt_config.num_replicas))]))
