# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sparse_grad.py
"""The backward operator for the SparseAdd op.

  The SparseAdd op calculates A + B, where A, B, and the sum are all represented
  as `SparseTensor` objects.  This op takes in the upstream gradient w.r.t.
  non-empty values of the sum, and outputs the gradients w.r.t. the non-empty
  values of A and B.

  Args:
    op: the SparseAdd op
    *grads: the incoming gradients, one element per output of `op`

  Returns:
    Gradient for each of the 6 input tensors of SparseAdd:
      (a_indices, a_values, a_shape, b_indices, b_values, b_shape, thresh)
    The gradients for the indices, shapes, and the threshold are None.
  """
val_grad = grads[1]
a_indices = op.inputs[0]
b_indices = op.inputs[3]
sum_indices = op.outputs[0]
# NOTE: we do not need to take `thresh` into account, since it simply affects
# the non-zero elements of the sum, and we will peek into `sum_indices` in the
# gradient op.

a_val_grad, b_val_grad = gen_sparse_ops.sparse_add_grad(
    val_grad, a_indices, b_indices, sum_indices)
a_val_grad.set_shape(op.inputs[1].get_shape())
b_val_grad.set_shape(op.inputs[4].get_shape())
# (a_indices, a_values, a_shape, b_indices, b_values, b_shape, thresh)
exit((None, a_val_grad, None, None, b_val_grad, None, None))
