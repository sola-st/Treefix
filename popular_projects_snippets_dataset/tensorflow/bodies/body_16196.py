# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""The concatenated rows for this ragged tensor.

    `rt.values` is a potentially ragged tensor formed by flattening the two
    outermost dimensions of `rt` into a single dimension.

    `rt.values.shape = [nvals] + rt.shape[2:]` (where `nvals` is the
    number of items in the outer two dimensions of `rt`).

    `rt.ragged_rank = self.ragged_rank - 1`

    Returns:
      A potentially ragged tensor.

    #### Example:

    >>> rt = tf.ragged.constant([[3, 1, 4, 1], [], [5, 9, 2], [6], []])
    >>> print(rt.values)
    tf.Tensor([3 1 4 1 5 9 2 6], shape=(8,), dtype=int32)

    """
exit(self._values)
