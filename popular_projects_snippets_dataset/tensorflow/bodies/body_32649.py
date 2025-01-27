# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linalg_ops_test.py
for n in range(1, 6):
    for np_dtype, atol in [(np.float32, 0.05), (np.float64, 1e-5),
                           (np.complex64, 0.05), (np.complex128, 1e-5)]:
        with self.subTest(n=n, np_dtype=np_dtype, atol=atol):
            matrix = _RandomPDMatrix(n, self.rng, np_dtype)
            _, logdet_np = np.linalg.slogdet(matrix)
            with self.session():
                # Create 2 x n x n matrix
                # matrix = np.array(
                #     [_RandomPDMatrix(n, self.rng, np_dtype),
                #      _RandomPDMatrix(n, self.rng, np_dtype)]).astype(np_dtype)
                logdet_tf = linalg.logdet(matrix)
                self.assertAllClose(logdet_np, self.evaluate(logdet_tf), atol=atol)
