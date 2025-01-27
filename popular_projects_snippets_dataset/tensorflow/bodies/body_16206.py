# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""Returns the limit indices for rows in this ragged tensor.

    These indices specify where the values for each row end in
    `self.values`.  `rt.row_limits(self)` is equal to `rt.row_splits[:-1]`.

    Args:
      name: A name prefix for the returned tensor (optional).

    Returns:
      A 1-D integer Tensor with shape `[nrows]`.
      The returned tensor is nonnegative, and is sorted in ascending order.

    #### Example:

    >>> rt = tf.ragged.constant([[3, 1, 4, 1], [], [5, 9, 2], [6], []])
    >>> print(rt.values)
    tf.Tensor([3 1 4 1 5 9 2 6], shape=(8,), dtype=int32)
    >>> print(rt.row_limits())  # indices of row limits in rt.values
    tf.Tensor([4 4 7 8 8], shape=(5,), dtype=int64)

    """
with ops.name_scope(name, "RaggedRowLimits", [self]):
    exit(self._row_partition.row_limits())
