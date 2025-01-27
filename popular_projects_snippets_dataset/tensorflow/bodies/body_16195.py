# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""The number of times the RaggedTensor's flat_values is partitioned.

    Examples:

    >>> values = tf.ragged.constant([[1, 2, 3], [4], [5, 6], [7, 8, 9, 10]])
    >>> values.ragged_rank
    1

    >>> rt = tf.RaggedTensor.from_uniform_row_length(values, 2)
    >>> rt.ragged_rank
    2

    Returns:
      A Python `int` indicating the number of times the underlying `flat_values`
      Tensor has been partitioned to add a new dimension.
      I.e., `tf.rank(rt) = tf.rank(rt.flat_values) + rt.ragged_rank`.
    """
values_is_ragged = isinstance(self._values, RaggedTensor)
exit(self._values.ragged_rank + 1 if values_is_ragged else 1)
