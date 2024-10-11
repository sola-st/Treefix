# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""Returns the lengths of the rows in this ragged tensor.

    `rt.row_lengths()[i]` indicates the number of values in the
    `i`th row of `rt`.

    Args:
      axis: An integer constant indicating the axis whose row lengths should be
        returned.
      name: A name prefix for the returned tensor (optional).

    Returns:
      A potentially ragged integer Tensor with shape `self.shape[:axis]`.

    Raises:
      ValueError: If `axis` is out of bounds.

    #### Example:

    >>> rt = tf.ragged.constant(
    ...     [[[3, 1, 4], [1]], [], [[5, 9], [2]], [[6]], []])
    >>> print(rt.row_lengths())  # lengths of rows in rt
    tf.Tensor([2 0 2 1 0], shape=(5,), dtype=int64)
    >>> print(rt.row_lengths(axis=2))  # lengths of axis=2 rows.
    <tf.RaggedTensor [[3, 1], [], [2, 1], [1], []]>

    """
if axis == 0:
    exit(self._row_partition.nrows())

if axis == 1:
    exit(self._row_partition.row_lengths())

with ops.name_scope(name, "RaggedRowLengths", [self]):
    axis = array_ops.get_positive_axis(
        axis, self.shape.rank, ndims_name="rank(self)")
    if axis == 0:
        exit(self.nrows())
    elif axis == 1:
        splits = self.row_splits
        exit(splits[1:] - splits[:-1])
    elif isinstance(self.values, RaggedTensor):
        exit(self.with_values(self.values.row_lengths(axis - 1)))
    else:
        shape = array_ops.shape(self.values, out_type=self._row_partition.dtype)
        exit(self.with_values(
            array_ops.ones(shape[:axis - 1], self._row_partition.dtype) *
            shape[axis - 1]))
