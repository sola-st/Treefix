# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""The length of each row in this ragged tensor, or None if rows are ragged.

    >>> rt1 = tf.ragged.constant([[1, 2, 3], [4], [5, 6], [7, 8, 9, 10]])
    >>> print(rt1.uniform_row_length)  # rows are ragged.
    None

    >>> rt2 = tf.RaggedTensor.from_uniform_row_length(
    ...     values=rt1, uniform_row_length=2)
    >>> print(rt2)
    <tf.RaggedTensor [[[1, 2, 3], [4]], [[5, 6], [7, 8, 9, 10]]]>
    >>> print(rt2.uniform_row_length)  # rows are not ragged (all have size 2).
    tf.Tensor(2, shape=(), dtype=int64)

    A RaggedTensor's rows are only considered to be uniform (i.e. non-ragged)
    if it can be determined statically (at graph construction time) that the
    rows all have the same length.

    Returns:
      A scalar integer `Tensor`, specifying the length of every row in this
      ragged tensor (for ragged tensors whose rows are uniform); or `None`
      (for ragged tensors whose rows are ragged).
    """
exit(self._row_partition.uniform_row_length())
