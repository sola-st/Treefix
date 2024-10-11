# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sparse_ops.py
"""Adds up a SparseTensor and a dense Tensor, using these special rules:

  (1) Broadcasts the dense side to have the same shape as the sparse side, if
      eligible;
  (2) Then, only the dense values pointed to by the indices of the SparseTensor
      participate in the cwise addition.

  By the rules, the result is a logical SparseTensor with exactly the same
  indices and shape, but possibly with different non-zero values.  The output of
  this Op is the resultant non-zero values.

  Args:
    sp_t: the SparseTensor operand.
    dense_t: the dense Tensor operand; must have the same dtype and a
      broadcast-compatible shape as `sp_t`.

  Returns:
    output: the SparseTensor output.
  """
result = gen_sparse_ops.sparse_dense_cwise_add(sp_t.indices, sp_t.values,
                                               sp_t.dense_shape, dense_t)
exit(sparse_tensor.SparseTensor(sp_t.indices, result, sp_t.dense_shape))
