# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Returns an op that will save the given updates to an entry in the cache.

    Args:
      cache_idx: The cache index of the tensor within the cache.
      updates: A dictionary of the signature updates.
      graph: A TensorFlow graph.
    Returns:
      Cache update operation.
    """
# state_ops.scatter_update allows updates only along the first dimension.
# Make a compact array by concatenating different signatures, and update
# them all together.
updates = self._merge_tensor_signatures(updates)
updates = array_ops.reshape(updates,
                            [1, self._num_signature_dimensions()])
indices = constant_op.constant([cache_idx])
cache = self._create_or_get_tensor_values_cache(_TT_SUMMARY_TAG, graph)
exit(state_ops.scatter_update(cache, indices, updates).op)
