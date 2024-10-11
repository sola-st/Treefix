# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/diag_op_test.py
# Diagonal bands.
# pyformat: disable
vecs = np.array([[[1, 2, 3, 4],  # Input shape: (2, 3, 4)
                  [5, 6, 7, 8],
                  [9, 8, 7, 6]],
                 [[5, 4, 3, 2],
                  [1, 2, 3, 4],
                  [5, 6, 7, 8]]])
tests = dict()
tests[-3, -1] = (vecs,
                 np.array([[[0, 0, 0, 0, 0],
                            [1, 0, 0, 0, 0],
                            [5, 2, 0, 0, 0],
                            [9, 6, 3, 0, 0],
                            [0, 8, 7, 4, 0]],
                           [[0, 0, 0, 0, 0],
                            [5, 0, 0, 0, 0],
                            [1, 4, 0, 0, 0],
                            [5, 2, 3, 0, 0],
                            [0, 6, 3, 2, 0]]]))
tests[-1, 1] = (vecs,
                np.array([[[5, 1, 0, 0],
                           [9, 6, 2, 0],
                           [0, 8, 7, 3],
                           [0, 0, 7, 8]],
                          [[1, 5, 0, 0],
                           [5, 2, 4, 0],
                           [0, 6, 3, 3],
                           [0, 0, 7, 4]]]))
tests[2, 4] = (vecs,
               np.array([[[0, 0, 9, 5, 1, 0],
                          [0, 0, 0, 8, 6, 2],
                          [0, 0, 0, 0, 7, 7],
                          [0, 0, 0, 0, 0, 6],
                          [0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0]],
                         [[0, 0, 5, 1, 5, 0],
                          [0, 0, 0, 6, 2, 4],
                          [0, 0, 0, 0, 7, 3],
                          [0, 0, 0, 0, 0, 8],
                          [0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0]]]))
# pyformat: enable
exit((None, repack_diagonals_in_tests(tests, align)))
