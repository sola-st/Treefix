# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linalg_ops_test.py
for np_dtype, atol in [(np.float32, 0.05), (np.float64, 1e-5),
                       (np.complex64, 0.05), (np.complex128, 1e-5)]:
    with self.subTest(np_dtype=np_dtype, atol=atol):
        matrix = (np.eye(20) * 1e-6).astype(np_dtype)
        _, logdet_np = np.linalg.slogdet(matrix)
        with self.session():
            logdet_tf = linalg.logdet(matrix)
            self.assertAllClose(logdet_np, self.evaluate(logdet_tf), atol=atol)
