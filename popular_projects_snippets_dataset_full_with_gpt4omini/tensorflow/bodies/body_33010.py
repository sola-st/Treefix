# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/cholesky_op_test.py
# Gradient is l^{-H} @ ((l^{H} @ grad) * (tril(ones)-1/2*eye)) @ l^{-1}

# Compute ((l^{H} @ grad) * (tril(ones)-1/2*eye)) = middle
middle = math_ops.matmul(l, grad, adjoint_a=True)
middle = array_ops.matrix_set_diag(middle,
                                   0.5 * array_ops.matrix_diag_part(middle))
middle = array_ops.matrix_band_part(middle, -1, 0)

# Compute l^{-H} @ middle = z
l_inverse_middle = linalg_ops.matrix_triangular_solve(l, middle, adjoint=True)

# We need to compute z @ l^{-1}. With matrix_triangular_solve we
# actually compute l^{-H} @ z^{H} = grad. Since we later add grad^{H}
# we can ommit the conjugate transpose here.
z_h = math_ops.conj(array_ops.matrix_transpose(l_inverse_middle))
grad_a = linalg_ops.matrix_triangular_solve(l, z_h, adjoint=True)
grad_a += linalg.adjoint(grad_a)
exit(grad_a * 0.5)
