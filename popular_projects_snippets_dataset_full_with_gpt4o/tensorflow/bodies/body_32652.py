# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linalg_ops_test.py
for n in range(1, 6):
    for np_dtype, atol in [(np.float32, 0.05), (np.float64, 1e-5),
                           (np.complex64, 0.05), (np.complex128, 1e-5)]:
        with self.subTest(n=n, np_dtype=np_dtype, atol=atol):
            matrix = _RandomPDMatrix(n, self.rng, np_dtype)
            sign_np, log_abs_det_np = np.linalg.slogdet(matrix)
            with self.session():
                sign_tf, log_abs_det_tf = linalg.slogdet(matrix)
                self.assertAllClose(
                    log_abs_det_np, self.evaluate(log_abs_det_tf), atol=atol)
                self.assertAllClose(sign_np, self.evaluate(sign_tf), atol=atol)
