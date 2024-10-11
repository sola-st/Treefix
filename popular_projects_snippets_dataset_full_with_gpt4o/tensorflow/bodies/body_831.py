# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/matrix_diag_ops_test.py
matrices = np.arange(3 * 2 * 4).reshape([3, 2, 4])
solution = np.array([[0, 5], [8, 13], [16, 21]])
self._assertOpOutputMatchesExpected({"input": matrices}, solution,
                                    high_level)
