# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_kronecker.py
# We heavily rely on Roth's column Lemma [1]:
# (A x B) * vec X = vec BXA^T
# where vec stacks all the columns of the matrix under each other.
# In our case, we use a variant of the lemma that is row-major
# friendly: (A x B) * vec' X = vec' AXB^T
# Where vec' reshapes a matrix into a vector. We can repeatedly apply this
# for a collection of kronecker products.
# Given that (A x B)^-1 = A^-1 x B^-1 and (A x B)^T = A^T x B^T, we can
# use the above to compute multiplications, solves with any composition of
# transposes.
output = x

if adjoint_arg:
    if self.dtype.is_complex:
        output = math_ops.conj(output)
else:
    output = linalg.transpose(output)

for o in reversed(self.operators):
    # Statically compute the reshape.
    if adjoint:
        operator_dimension = o.range_dimension_tensor()
    else:
        operator_dimension = o.domain_dimension_tensor()
    output_shape = _prefer_static_shape(output)

    if tensor_util.constant_value(operator_dimension) is not None:
        operator_dimension = tensor_util.constant_value(operator_dimension)
        if output.shape[-2] is not None and output.shape[-1] is not None:
            dim = int(output.shape[-2] * output_shape[-1] // operator_dimension)
    else:
        dim = math_ops.cast(
            output_shape[-2] * output_shape[-1] // operator_dimension,
            dtype=dtypes.int32)

    output_shape = _prefer_static_concat_shape(
        output_shape[:-2], [dim, operator_dimension])
    output = array_ops.reshape(output, shape=output_shape)

    # Conjugate because we are trying to compute A @ B^T, but
    # `LinearOperator` only supports `adjoint_arg`.
    if self.dtype.is_complex:
        output = math_ops.conj(output)

    output = solve_matmul_fn(
        o, output, adjoint=adjoint, adjoint_arg=True)

if adjoint_arg:
    col_dim = _prefer_static_shape(x)[-2]
else:
    col_dim = _prefer_static_shape(x)[-1]

if adjoint:
    row_dim = self.domain_dimension_tensor()
else:
    row_dim = self.range_dimension_tensor()

matrix_shape = [row_dim, col_dim]

output = array_ops.reshape(
    output,
    _prefer_static_concat_shape(
        _prefer_static_shape(output)[:-2], matrix_shape))

if x.shape.is_fully_defined():
    if adjoint_arg:
        column_dim = x.shape[-2]
    else:
        column_dim = x.shape[-1]
    broadcast_batch_shape = common_shapes.broadcast_shape(
        x.shape[:-2], self.batch_shape)
    if adjoint:
        matrix_dimensions = [self.domain_dimension, column_dim]
    else:
        matrix_dimensions = [self.range_dimension, column_dim]

    output.set_shape(broadcast_batch_shape.concatenate(
        matrix_dimensions))

exit(output)
