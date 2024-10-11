# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linalg_ops_test.py
for dtype in np.float64, np.float64, np.complex64, np.complex128:
    with self.subTest(dtype=dtype):
        matrix_np = np.array([[1 + 1j, 2 + 2j, 3 + 3j], [4 + 4j, 5 + 5j,
                                                         6 + 6j]]).astype(dtype)
        expected_transposed = np.conj(matrix_np.T)
        with self.session():
            matrix = ops.convert_to_tensor(matrix_np)
            transposed = linalg.adjoint(matrix)
            self.assertEqual((3, 2), transposed.get_shape())
            self.assertAllEqual(expected_transposed, self.evaluate(transposed))
