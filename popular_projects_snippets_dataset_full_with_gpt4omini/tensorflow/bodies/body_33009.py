# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/cholesky_op_test.py
middle = math_ops.matmul(l, grad, adjoint_a=True)
middle = array_ops.matrix_set_diag(middle,
                                   0.5 * array_ops.matrix_diag_part(middle))
middle = array_ops.matrix_band_part(middle, -1, 0)
grad_a = math_ops.matmul(
    math_ops.matmul(l_inverse, middle, adjoint_a=True), l_inverse)
grad_a += math_ops.conj(array_ops.matrix_transpose(grad_a))
exit(grad_a * 0.5)
