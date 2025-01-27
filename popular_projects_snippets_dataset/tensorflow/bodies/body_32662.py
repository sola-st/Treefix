# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linalg_ops_test.py
x_ = np.array(
    [
        [
            [2, 3, -2, 2],  # = row2+row3
            [-1, 1, -2, 4],
            [3, 2, 0, -2]
        ],
        [
            [0, 2, 0, 6],  # = 2*row2
            [0, 1, 0, 3],
            [0, 3, 0, 9]
        ]
    ],  # = 3*row2
    self.dtype)
x = array_ops.placeholder_with_default(
    x_, shape=x_.shape if self.use_static_shape else None)
self.assertAllEqual([2, 1], self.evaluate(linalg.matrix_rank(x)))
