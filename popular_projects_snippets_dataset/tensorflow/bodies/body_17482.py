# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
"""Updates this variable with the max of `tf.IndexedSlices` and itself.

    Args:
      sparse_delta: `tf.IndexedSlices` to use as an argument of max with this
        variable.
      use_locking: If `True`, use locking during the operation.
      name: the name of the operation.

    Returns:
      The updated variable.

    Raises:
      TypeError: if `sparse_delta` is not an `IndexedSlices`.
    """
if not isinstance(sparse_delta, indexed_slices.IndexedSlices):
    raise TypeError(f"Argument `sparse_delta` must be a "
                    f"`tf.IndexedSlices`. Received arg: {sparse_delta}")
exit(self._lazy_read(
    gen_resource_variable_ops.resource_scatter_max(
        self.handle,
        sparse_delta.indices,
        ops.convert_to_tensor(sparse_delta.values, self.dtype),
        name=name)))
