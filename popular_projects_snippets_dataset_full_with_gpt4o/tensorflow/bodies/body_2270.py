# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/binary_ops_test.py
for dtype, pad_type in itertools.product(self.numeric_types,
                                         [np.int32, np.int64]):
    self._testBinary(
        array_ops.pad,
        np.array([[1, 2, 3], [4, 5, 6]], dtype=dtype),
        np.array([[1, 2], [2, 1]], dtype=pad_type),
        expected=np.array(
            [[0, 0, 0, 0, 0, 0], [0, 0, 1, 2, 3, 0], [0, 0, 4, 5, 6, 0],
             [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]],
            dtype=dtype))

    self._testBinary(
        lambda x, y: array_ops.pad(x, y, constant_values=7),
        np.array([[1, 2, 3], [4, 5, 6]], dtype=dtype),
        np.array([[0, 3], [2, 1]], dtype=pad_type),
        expected=np.array(
            [[7, 7, 1, 2, 3, 7], [7, 7, 4, 5, 6, 7], [7, 7, 7, 7, 7, 7],
             [7, 7, 7, 7, 7, 7], [7, 7, 7, 7, 7, 7]],
            dtype=dtype))
