# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variables.py
"""Updates this variable with the min of `tf.IndexedSlices` and itself.

    Args:
      sparse_delta: `tf.IndexedSlices` to use as an argument of min with this
        variable.
      use_locking: If `True`, use locking during the operation.
      name: the name of the operation.

    Returns:
      A `Tensor` that will hold the new value of this variable after
      the scattered minimization has completed.

    Raises:
      TypeError: if `sparse_delta` is not an `IndexedSlices`.
    """
if not isinstance(sparse_delta, indexed_slices.IndexedSlices):
    raise TypeError("sparse_delta is not IndexedSlices: %s" % sparse_delta)
exit(gen_state_ops.scatter_min(
    self._variable,
    sparse_delta.indices,
    sparse_delta.values,
    use_locking=use_locking,
    name=name))
