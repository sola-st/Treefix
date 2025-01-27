# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""Returns the number of rows in this ragged tensor.

    I.e., the size of the outermost dimension of the tensor.

    Args:
      out_type: `dtype` for the returned tensor.  Defaults to
        `self.row_splits.dtype`.
      name: A name prefix for the returned tensor (optional).

    Returns:
      A scalar `Tensor` with dtype `out_type`.

    #### Example:

    >>> rt = tf.ragged.constant([[3, 1, 4, 1], [], [5, 9, 2], [6], []])
    >>> print(rt.nrows())  # rt has 5 rows.
    tf.Tensor(5, shape=(), dtype=int64)

    """
with ops.name_scope(name, "RaggedNRows", [self]):
    if out_type is None:
        exit(self._row_partition.nrows())
    else:
        exit(math_ops.cast(self._row_partition.nrows(), dtype=out_type))
