# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sparse_grad.py
"""Gradients for the dense tensor in the SparseTensorDenseMatMul op.

  Args:
    op: the SparseTensorDenseMatMul op
    grad: the incoming gradient

  Returns:
    Gradient for each of the 4 input tensors:
      (sparse_indices, sparse_values, sparse_shape, dense_tensor)
    The gradients for indices and shape are None.

  Raises:
    TypeError: When the two operands don't have the same type.
  """
a_indices, a_values, a_shape = op.inputs[:3]
b = op.inputs[3]
adj_a = op.get_attr("adjoint_a")
adj_b = op.get_attr("adjoint_b")

a_type = a_values.dtype.base_dtype
b_type = b.dtype.base_dtype
if a_type != b_type:
    raise TypeError(
        f"SparseTensorDenseMatMul op received operands with different types: "
        f"`{a_type}` and `{b_type}`.")

# gradient w.r.t. dense
b_grad = gen_sparse_ops.sparse_tensor_dense_mat_mul(
    a_indices, a_values, a_shape, grad, adjoint_a=not adj_a)
if adj_b:
    b_grad = array_ops.matrix_transpose(b_grad, conjugate=True)

# gradient w.r.t. sparse values

# TODO(zongheng): these gather calls could potentially duplicate rows/cols in
# memory.  If there is a need, we should look into implementing this more
# intelligently to avoid duplicating data.

# With no adjoints, a_grad is matmul(grad, adjoint(b)). Since a is sparse, we
# just want to compute that matmul at the rows/columns of non-zero values. The
# (r, c) value is sum(grad[r, :] * adjoint(b)[:, c]), where the latter term is
# more conveniently written as conj(b)[c, :]. That expression is more
# efficient to calculate as a matmul, after expanding the two terms to be 2D
# (i.e. a row vector and a column vector).
#
# If adj_b then we replace conj(b) by transpose(b); if adj_a we need to
# adjoint the result, which is equivalent to swapping r and c and taking
# conjugates.

# Get grad[r, :] and b[c, :] (or with r and c swapped if adj_a, or with
# transpose(b) if adj_b), as batches of vectors (with the batch dimension
# corresponding to the non-zero indices of a).
rows = a_indices[:, 0]
cols = a_indices[:, 1]
parts_a = array_ops.gather(grad, rows if not adj_a else cols)
parts_b = array_ops.gather(
    b if not adj_b else array_ops.transpose(b), cols if not adj_a else rows)

if not adj_a and not adj_b:
    # grad[r, :] * conj(b[c, :]) = row(grad[r, :]) @ adjoint(row(b[c, :]))
    a_values_grad = math_ops.matmul(
        array_ops.expand_dims(parts_a, -2),
        array_ops.expand_dims(parts_b, -2),
        adjoint_b=True)
elif adj_a and not adj_b:
    # conj(grad[c, :] * conj(b[r, :])) = adjoint(col(grad[c, :])) @ col(b[r, :])
    a_values_grad = math_ops.matmul(
        array_ops.expand_dims(parts_a, -1),
        array_ops.expand_dims(parts_b, -1),
        adjoint_a=True)
elif not adj_a and adj_b:
    # grad[r, :] * transpose(b)[c, :] =
    #     row(grad[r, :]) @ col(transpose(b)[c, :])
    a_values_grad = math_ops.matmul(
        array_ops.expand_dims(parts_a, -2), array_ops.expand_dims(parts_b, -1))
elif adj_a and adj_b:
    # conj(grad[c, :] * transpose(b)[r, :]) =
    #     adjoint(col(grad[c, :])) @ adjoint(row(transpose(b)[r, :])
    a_values_grad = math_ops.matmul(
        array_ops.expand_dims(parts_a, -1),
        array_ops.expand_dims(parts_b, -2),
        adjoint_a=True,
        adjoint_b=True)

# gradients w.r.t. (a_indices, a_values, a_shape, b)
exit((None, array_ops.squeeze(a_values_grad, axis=[-2, -1]), None, b_grad))
