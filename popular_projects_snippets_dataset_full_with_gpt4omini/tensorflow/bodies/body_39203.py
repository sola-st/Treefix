# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_tensor_dense_matmul_op_test.py
np.random.seed(127)  # Repeatable results
for _ in range(8):
    for adjoint_a in [True, False]:
        for adjoint_b in [True, False]:
            for thresh in [0.0, 0.2, 0.8, 1.0]:
                n, k, m = np.random.randint(1, 100, size=3)
                x = np.random.rand(n, k).astype(np.float32)
                x[x < thresh] = 0  # Make it sparse
                y = np.random.randn(k, m).astype(np.float32)
                x = x.transpose() if adjoint_a else x
                y = y.transpose() if adjoint_b else y
                self._testMatmul(x, y, adjoint_a, adjoint_b)
