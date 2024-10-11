# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/where_op_test.py
x = np.asarray([[[True, False], [True, False]],
                [[False, True], [False, True]],
                [[False, False], [False, True]]])

# Ensure RowMajor mode
truth = np.asarray(
    [[0, 0, 0], [0, 1, 0], [1, 0, 1], [1, 1, 1], [2, 1, 1]], dtype=np.int64)

self._testWhere(x, truth, None, fn)
