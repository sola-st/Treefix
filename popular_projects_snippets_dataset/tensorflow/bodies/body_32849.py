# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/svd_op_test.py
# Tests that a ~= u*diag(s)*transpose(v).
batch_shape = a.shape[:-2]
m = a.shape[-2]
n = a.shape[-1]
diag_s = math_ops.cast(array_ops.matrix_diag(s), dtype=dtype_)
if full_matrices_:
    if m > n:
        zeros = array_ops.zeros(batch_shape + (m - n, n), dtype=dtype_)
        diag_s = array_ops.concat([diag_s, zeros], a.ndim - 2)
    elif n > m:
        zeros = array_ops.zeros(batch_shape + (m, n - m), dtype=dtype_)
        diag_s = array_ops.concat([diag_s, zeros], a.ndim - 1)
a_recon = math_ops.matmul(u, diag_s)
a_recon = math_ops.matmul(a_recon, v, adjoint_b=True)
self.assertAllClose(a_recon, a, rtol=tol, atol=tol)
