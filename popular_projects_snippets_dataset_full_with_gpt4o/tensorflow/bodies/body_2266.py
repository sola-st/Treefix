# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/binary_ops_test.py
# Tests with batches of matrices.
for dtype in self.float_types | {np.float64}:
    self._testBinary(
        math_ops.matmul,
        np.array([[[-0.25]]], dtype=dtype),
        np.array([[[8]]], dtype=dtype),
        expected=np.array([[[-2]]], dtype=dtype))
    self._testBinary(
        math_ops.matmul,
        np.array([[[-0.25]], [[4]]], dtype=dtype),
        np.array([[[8]], [[2]]], dtype=dtype),
        expected=np.array([[[-2]], [[8]]], dtype=dtype))
    self._testBinary(
        math_ops.matmul,
        np.array([[[[7, 13], [10, 1]], [[2, 0.25], [20, 2]]],
                  [[[3, 5], [30, 3]], [[0.75, 1], [40, 4]]]],
                 dtype=dtype),
        np.array([[[[1, 2], [3, 4]], [[5, 6], [7, 8]]],
                  [[[11, 22], [33, 44]], [[55, 66], [77, 88]]]],
                 dtype=dtype),
        expected=np.array(
            [[[[46, 66], [13, 24]], [[11.75, 14], [114, 136]]],
             [[[198, 286], [429, 792]], [[118.25, 137.5], [2508, 2992]]]],
            dtype=dtype))

    self._testBinary(
        math_ops.matmul,
        np.array([], dtype=dtype).reshape((2, 2, 0)),
        np.array([], dtype=dtype).reshape((2, 0, 3)),
        expected=np.array([[[0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0]]],
                          dtype=dtype))
    self._testBinary(
        math_ops.matmul,
        np.array([], dtype=dtype).reshape((0, 2, 4)),
        np.array([], dtype=dtype).reshape((0, 4, 3)),
        expected=np.array([], dtype=dtype).reshape(0, 2, 3))  # pylint: disable=too-many-function-args

    # Regression test for b/31472796.
    if dtype != np.float16 and hasattr(np, "matmul"):
        x = np.arange(0, 3 * 5 * 2 * 7, dtype=dtype).reshape((3, 5, 2, 7))
        self._testBinary(
            lambda x, y: math_ops.matmul(x, y, adjoint_b=True),
            x,
            x,
            expected=np.matmul(x, x.transpose([0, 1, 3, 2])))
