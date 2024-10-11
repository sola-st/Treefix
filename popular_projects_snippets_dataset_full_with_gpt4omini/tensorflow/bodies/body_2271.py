# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/binary_ops_test.py
mirror_pad = lambda t, paddings: array_ops.pad(t, paddings, "SYMMETRIC")
for dtype in self.numeric_types:
    self._testBinary(
        mirror_pad,
        np.array(
            [
                [1, 2, 3],  #
                [4, 5, 6],  #
            ],
            dtype=dtype),
        np.array([[
            2,
            2,
        ], [3, 3]], dtype=np.int32),
        expected=np.array(
            [
                [6, 5, 4, 4, 5, 6, 6, 5, 4],  #
                [3, 2, 1, 1, 2, 3, 3, 2, 1],  #
                [3, 2, 1, 1, 2, 3, 3, 2, 1],  #
                [6, 5, 4, 4, 5, 6, 6, 5, 4],  #
                [6, 5, 4, 4, 5, 6, 6, 5, 4],  #
                [3, 2, 1, 1, 2, 3, 3, 2, 1],  #
            ],
            dtype=dtype))
    self._testBinary(
        mirror_pad,
        np.array([[1, 2, 3], [4, 5, 6]], dtype=dtype),
        np.array([[0, 0], [0, 0]], dtype=np.int32),
        expected=np.array([[1, 2, 3], [4, 5, 6]], dtype=dtype))
