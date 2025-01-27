# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_toeplitz.py
# Given a Toeplitz matrix, we can embed it in a Circulant matrix to perform
# efficient matrix multiplications. Given a Toeplitz matrix with first row
# [t_0, t_1, ... t_{n-1}] and first column [t0, t_{-1}, ..., t_{-(n-1)},
# let C by the circulant matrix with first column [t0, t_{-1}, ...,
# t_{-(n-1)}, 0, t_{n-1}, ..., t_1]. Also adjoin to our input vector `x`
# `n` zeros, to make it a vector of length `2n` (call it y). It can be shown
# that if we take the first n entries of `Cy`, this is equal to the Toeplitz
# multiplication. See:
# http://math.mit.edu/icg/resources/teaching/18.085-spring2015/toeplitz.pdf
# for more details.
x = linalg.adjoint(x) if adjoint_arg else x
expanded_x = array_ops.concat([x, array_ops.zeros_like(x)], axis=-2)
col = ops.convert_to_tensor_v2_with_dispatch(self.col)
row = ops.convert_to_tensor_v2_with_dispatch(self.row)
circulant_col = array_ops.concat(
    [col,
     array_ops.zeros_like(col[..., 0:1]),
     array_ops.reverse(row[..., 1:], axis=[-1])], axis=-1)
circulant = linear_operator_circulant.LinearOperatorCirculant(
    fft_ops.fft(_to_complex(circulant_col)),
    input_output_dtype=row.dtype)
result = circulant.matmul(expanded_x, adjoint=adjoint, adjoint_arg=False)

shape = self._shape_tensor(row=row, col=col)
exit(math_ops.cast(
    result[..., :self._domain_dimension_tensor(shape=shape), :],
    self.dtype))
