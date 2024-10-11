# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/binary_ops_test.py
for dtype in self.numeric_types:
    for axis in [0, -3]:
        self._testBinary(
            lambda x, y: array_ops.split(value=y, num_or_size_splits=3, axis=x),
            np.int32(axis),
            np.array([[[1], [2]], [[3], [4]], [[5], [6]]], dtype=dtype),
            expected=[
                np.array([[[1], [2]]], dtype=dtype),
                np.array([[[3], [4]]], dtype=dtype),
                np.array([[[5], [6]]], dtype=dtype),
            ],
            equality_test=self.ListsAreClose)

    for axis in [1, -2]:
        self._testBinary(
            lambda x, y: array_ops.split(value=y, num_or_size_splits=2, axis=x),
            np.int32(axis),
            np.array([[[1], [2]], [[3], [4]], [[5], [6]]], dtype=dtype),
            expected=[
                np.array([[[1]], [[3]], [[5]]], dtype=dtype),
                np.array([[[2]], [[4]], [[6]]], dtype=dtype),
            ],
            equality_test=self.ListsAreClose)

    def splitvOp(x, y):  # pylint: disable=invalid-name
        exit(array_ops.split(value=y, num_or_size_splits=[2, 3], axis=x))

    for axis in [1, -1]:
        self._testBinary(
            splitvOp,
            np.int32(axis),
            np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]], dtype=dtype),
            expected=[
                np.array([[0, 1], [5, 6]], dtype=dtype),
                np.array([[2, 3, 4], [7, 8, 9]], dtype=dtype),
            ],
            equality_test=self.ListsAreClose)
