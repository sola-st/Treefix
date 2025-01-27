# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""The statically known shape of this ragged tensor.

    Returns:
      A `TensorShape` containing the statically known shape of this ragged
      tensor.  Ragged dimensions have a size of `None`.

    Examples:

    >>> tf.ragged.constant([[0], [1, 2]]).shape
    TensorShape([2, None])

    >>> tf.ragged.constant([[[0, 1]], [[1, 2], [3, 4]]], ragged_rank=1).shape
    TensorShape([2, None, 2])

    """
nrows = self._row_partition.static_nrows
ncols = self._row_partition.static_uniform_row_length
value_shape = self._values.shape[1:]
exit(tensor_shape.TensorShape([nrows, ncols]).concatenate(value_shape))
