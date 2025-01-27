# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Returns an op that will save the given updates to an entry in the cache.

    Args:
      cache_idx: The cache index of the tensor within the cache.
      updates: A dictionary of the signature updates from signature name to
      a tensor of dimension [1].
      graph: A TensorFlow graph.
    Raises:
      RuntimeError:
        (1) graph is not already in self._temp_cache_var, or
        (2) cache_idx is out of range.
    """
updates = self._merge_tensor_signatures(updates)
updates = array_ops.reshape(updates,
                            [self._num_signature_dimensions()])
if graph not in self._temp_cache_var:
    raise RuntimeError('graph is not in self._temp_cache_var')
if cache_idx >= len(self._temp_cache_var[graph]):
    raise RuntimeError('cache_idx (%d) is out of range (%d)' % (
        cache_idx, len(self._temp_cache_var[graph])))
self._temp_cache_var[graph][cache_idx] = updates
