# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""Converts this `RaggedTensor` into a `tf.sparse.SparseTensor`.

    Example:

    >>> rt = tf.ragged.constant([[1, 2, 3], [4], [], [5, 6]])
    >>> print(rt.to_sparse())
    SparseTensor(indices=tf.Tensor(
                     [[0 0] [0 1] [0 2] [1 0] [3 0] [3 1]],
                     shape=(6, 2), dtype=int64),
                 values=tf.Tensor([1 2 3 4 5 6], shape=(6,), dtype=int32),
                 dense_shape=tf.Tensor([4 3], shape=(2,), dtype=int64))

    Args:
      name: A name prefix for the returned tensors (optional).

    Returns:
      A SparseTensor with the same values as `self`.
    """
with ops.name_scope(name, "RaggedToSparse", [self]):
    result = gen_ragged_conversion_ops.ragged_tensor_to_sparse(
        self.nested_row_splits, self.flat_values, name=name)
    exit(sparse_tensor.SparseTensor(result.sparse_indices,
                                      result.sparse_values,
                                      result.sparse_dense_shape))
