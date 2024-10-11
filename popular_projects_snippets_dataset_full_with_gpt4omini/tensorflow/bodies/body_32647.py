# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linalg_ops_test.py
for n in range(1, 6):
    for np_type, atol in [(np.float32, 0.05), (np.float64, 1e-5)]:
        with self.session():
            # Create 2 x n x n matrix
            array = np.array(
                [_RandomPDMatrix(n, self.rng),
                 _RandomPDMatrix(n, self.rng)]).astype(np_type)
            chol = linalg_ops.cholesky(array)
            for k in range(1, 3):
                with self.subTest(n=n, np_type=np_type, atol=atol, k=k):
                    rhs = self.rng.randn(2, n, k).astype(np_type)
                    x = linalg_ops.cholesky_solve(chol, rhs)
                    self.assertAllClose(rhs, math_ops.matmul(array, x), atol=atol)
