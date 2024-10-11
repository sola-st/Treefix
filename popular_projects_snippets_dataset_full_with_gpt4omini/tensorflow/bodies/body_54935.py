# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/sparse_tensor.py
"""Returns a copy of `self` with `values` replaced by `new_values`.

    This method produces a new `SparseTensor` that has the same nonzero
    `indices` and same `dense_shape`, but updated values.

    Args:
      new_values: The values of the new `SparseTensor`. Needs to have the same
        shape as the current `.values` `Tensor`. May have a different type than
        the current `values`.

    Returns:
      A `SparseTensor` with identical indices and shape but updated values.

    Example usage:

    >>> st = tf.sparse.from_dense([[1, 0, 2, 0], [3, 0, 0, 4]])
    >>> tf.sparse.to_dense(st.with_values([10, 20, 30, 40]))  # 4 nonzero values
    <tf.Tensor: shape=(2, 4), dtype=int32, numpy=
    array([[10,  0, 20,  0],
           [30,  0,  0, 40]], dtype=int32)>

    """
exit(SparseTensor(self._indices, new_values, self._dense_shape))
