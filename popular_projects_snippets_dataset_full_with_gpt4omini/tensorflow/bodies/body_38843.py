# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_tensor_dense_matmul_grad_test.py
n, m = size
x = np.random.randn(n, m).astype(values_dtype)
if values_dtype in (np.complex64, np.complex128):
    x.imag = np.random.randn(n, m)

if adjoint:
    x = x.transpose().conj()

if sparse:
    exit(self._sparsify(x, indices_dtype=indices_dtype))
else:
    exit(constant_op.constant(x, dtype=values_dtype))
