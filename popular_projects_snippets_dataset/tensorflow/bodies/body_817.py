# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/matrix_diag_ops_test.py
# pyformat: disable
vecs1 = np.array([[1, 2],
                  [3, 4]])
solution1 = np.array([[[1, 0], [0, 2]],
                      [[3, 0], [0, 4]]])
vecs2 = np.array([1, 2, 3, 4])
solution2 = np.array([[1, 0, 0, 0],
                      [0, 2, 0, 0],
                      [0, 0, 3, 0],
                      [0, 0, 0, 4]])
vecs3 = np.array([[[1, 2, 3],
                   [4, 5, 6]],
                  [[7,  8,  9],  # pylint: disable=bad-whitespace
                   [10, 11, 12]]])
solution3 = np.array([[[[1, 0, 0],
                        [0, 2, 0],
                        [0, 0, 3]],
                       [[4, 0, 0],
                        [0, 5, 0],
                        [0, 0, 6]]],
                      [[[7, 0, 0],
                        [0, 8, 0],
                        [0, 0, 9]],
                       [[10, 0, 0],
                        [0, 11, 0],
                        [0, 0, 12]]]])
# pyformat: enable
self._assertOpOutputMatchesExpected({"diagonal": vecs1}, solution1,
                                    high_level)
self._assertOpOutputMatchesExpected({"diagonal": vecs2}, solution2,
                                    high_level)
self._assertOpOutputMatchesExpected({"diagonal": vecs3}, solution3,
                                    high_level)
