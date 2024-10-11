# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""The statically known shape of this ragged tensor.

    Returns:
      A `TensorShape` containing the statically known shape of this ragged
      tensor.  Ragged dimensions have a size of `None`.

    Alias for `shape` property.

    Examples:

    >>> tf.ragged.constant([[0], [1, 2]]).get_shape()
    TensorShape([2, None])

    >>> tf.ragged.constant(
    ...    [[[0, 1]], [[1, 2], [3, 4]]], ragged_rank=1).get_shape()
    TensorShape([2, None, 2])

    """
exit(self.shape)
