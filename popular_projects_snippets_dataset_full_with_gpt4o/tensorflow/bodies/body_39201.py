# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_tensor_dense_matmul_op_test.py
r1 = np.random.randint(6000, 20000)
r2 = np.random.randint(1, 10)
r3 = np.random.randint(1, 10)

for m, k, n in [(r1, r2, r3),
                (r2, r1, r3),
                (r2, r3, r1)]:
    x = _maybe_complex(np.random.rand(m, k).astype(np_dtype))
    x[np.abs(x) < 0.8] = 0

    y = _maybe_complex(np.random.randn(k, n).astype(np_dtype))

    self._testMatmul(x, y, adjoint_a=False, adjoint_b=False)
    self._testMatmul(x.transpose(), y, adjoint_a=True, adjoint_b=False)
    self._testMatmul(x, y.transpose(), adjoint_a=False, adjoint_b=True)
    self._testMatmul(
        x.transpose(), y.transpose(), adjoint_a=True, adjoint_b=True)
