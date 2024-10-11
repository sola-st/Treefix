# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sparse_grad.py
"""The backward operator for the SparseSlice op.

  This op takes in the upstream gradient w.r.t. non-empty values of
  the sliced `SparseTensor`, and outputs the gradients w.r.t.
  the non-empty values of input `SparseTensor`.

  Args:
    op: the SparseSlice op
    *grads: the incoming gradients, one element per output of `op`

  Returns:
    Gradient for each of the 5 input tensors of SparseSlice:
      (indices, values, shape, start, size)
    The gradients for the indices, shape, start and the size are None.
  """
backprop_val_grad = grads[1]
input_indices = op.inputs[0]
input_start = op.inputs[3]
output_indices = op.outputs[0]

val_grad = gen_sparse_ops.sparse_slice_grad(backprop_val_grad, input_indices,
                                            input_start, output_indices)
val_grad.set_shape(op.inputs[1].get_shape())
# (indices, values, shape, start, size)
exit((None, val_grad, None, None, None))
