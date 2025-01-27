# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/binary_ops_test.py
mirror_pad = lambda t, paddings: array_ops.pad(t, paddings, "REFLECT")
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
            1,
            1,
        ], [2, 2]], dtype=np.int32),
        expected=np.array(
            [
                [6, 5, 4, 5, 6, 5, 4],  #
                [3, 2, 1, 2, 3, 2, 1],  #
                [6, 5, 4, 5, 6, 5, 4],  #
                [3, 2, 1, 2, 3, 2, 1]
            ],
            dtype=dtype))
    self._testBinary(
        mirror_pad,
        np.array([[1, 2, 3], [4, 5, 6]], dtype=dtype),
        np.array([[0, 0], [0, 0]], dtype=np.int32),
        expected=np.array([[1, 2, 3], [4, 5, 6]], dtype=dtype))
    self._testBinary(
        mirror_pad,
        np.array(
            [
                [1, 2, 3],  #
                [4, 5, 6],  #
                [7, 8, 9]
            ],
            dtype=dtype),
        np.array([[2, 2], [0, 0]], dtype=np.int32),
        expected=np.array(
            [
                [7, 8, 9],  #
                [4, 5, 6],  #
                [1, 2, 3],  #
                [4, 5, 6],  #
                [7, 8, 9],  #
                [4, 5, 6],  #
                [1, 2, 3]
            ],
            dtype=dtype))
    self._testBinary(
        mirror_pad,
        np.array([
            [[1, 2, 3], [4, 5, 6]],
            [[7, 8, 9], [10, 11, 12]],
        ],
                 dtype=dtype),
        np.array([[0, 0], [1, 1], [1, 1]], dtype=np.int32),
        expected=np.array(
            [
                [
                    [5, 4, 5, 6, 5],  #
                    [2, 1, 2, 3, 2],  #
                    [5, 4, 5, 6, 5],  #
                    [2, 1, 2, 3, 2],  #
                ],
                [
                    [11, 10, 11, 12, 11],  #
                    [8, 7, 8, 9, 8],  #
                    [11, 10, 11, 12, 11],  #
                    [8, 7, 8, 9, 8],  #
                ]
            ],
            dtype=dtype))
