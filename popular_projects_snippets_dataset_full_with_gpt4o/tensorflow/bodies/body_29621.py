# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/diag_op_test.py
# pyformat: disable
mat = np.array([[[1, 2, 3, 4, 5],
                 [6, 7, 8, 9, 1],
                 [3, 4, 5, 6, 7],
                 [8, 9, 1, 2, 3],
                 [4, 5, 6, 7, 8]],
                [[9, 1, 2, 3, 4],
                 [5, 6, 7, 8, 9],
                 [1, 2, 3, 4, 5],
                 [6, 7, 8, 9, 1],
                 [2, 3, 4, 5, 6]]])
tests = dict()
# tests[d_lower, d_upper] = (packed_diagonals, padded_diagonals)
tests[-1, -1] = (np.array([[6, 4, 1, 7],
                           [5, 2, 8, 5]]),
                 np.array([[[0, 0, 0, 0, 0],
                            [6, 0, 0, 0, 0],
                            [0, 4, 0, 0, 0],
                            [0, 0, 1, 0, 0],
                            [0, 0, 0, 7, 0]],
                           [[0, 0, 0, 0, 0],
                            [5, 0, 0, 0, 0],
                            [0, 2, 0, 0, 0],
                            [0, 0, 8, 0, 0],
                            [0, 0, 0, 5, 0]]]))
tests[-4, -3] = (np.array([[[8, 5],
                            [4, 0]],
                           [[6, 3],
                            [2, 0]]]),
                 np.array([[[0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0],
                            [8, 0, 0, 0, 0],
                            [4, 5, 0, 0, 0]],
                           [[0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0],
                            [6, 0, 0, 0, 0],
                            [2, 3, 0, 0, 0]]]))
tests[-2, 1] = (np.array([[[2, 8, 6, 3, 0],
                           [1, 7, 5, 2, 8],
                           [6, 4, 1, 7, 0],
                           [3, 9, 6, 0, 0]],
                          [[1, 7, 4, 1, 0],
                           [9, 6, 3, 9, 6],
                           [5, 2, 8, 5, 0],
                           [1, 7, 4, 0, 0]]]),
                np.array([[[1, 2, 0, 0, 0],
                           [6, 7, 8, 0, 0],
                           [3, 4, 5, 6, 0],
                           [0, 9, 1, 2, 3],
                           [0, 0, 6, 7, 8]],
                          [[9, 1, 0, 0, 0],
                           [5, 6, 7, 0, 0],
                           [1, 2, 3, 4, 0],
                           [0, 7, 8, 9, 1],
                           [0, 0, 4, 5, 6]]]))
tests[2, 4] = (np.array([[[5, 0, 0],
                          [4, 1, 0],
                          [3, 9, 7]],
                         [[4, 0, 0],
                          [3, 9, 0],
                          [2, 8, 5]]]),
               np.array([[[0, 0, 3, 4, 5],
                          [0, 0, 0, 9, 1],
                          [0, 0, 0, 0, 7],
                          [0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0]],
                         [[0, 0, 2, 3, 4],
                          [0, 0, 0, 8, 9],
                          [0, 0, 0, 0, 5],
                          [0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0]]]))  # pyformat: enable
exit((mat, repack_diagonals_in_tests(tests, align)))
