# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/unary_ops_test.py
for dtype in self.numeric_types - {np.int8, np.uint8}:
    self._assertOpOutputMatchesExpected(
        array_ops.diag, np.array([1, 2, 3, 4], dtype=dtype),
        np.array(
            [[1, 0, 0, 0], [0, 2, 0, 0], [0, 0, 3, 0], [0, 0, 0, 4]],
            dtype=dtype))
    self._assertOpOutputMatchesExpected(
        array_ops.diag_part,
        np.arange(36).reshape([2, 3, 2, 3]).astype(dtype),
        np.array([[0, 7, 14], [21, 28, 35]], dtype=dtype))
    self._assertOpOutputMatchesExpected(
        array_ops.diag, np.array([[1, 2], [3, 4]], dtype=dtype),
        np.array(
            [[[[1, 0], [0, 0]], [[0, 2], [0, 0]]], [[[0, 0], [3, 0]],
                                                    [[0, 0], [0, 4]]]],
            dtype=dtype))

    self._assertOpOutputMatchesExpected(
        array_ops.identity,
        np.array([[-1, 1]], dtype=dtype),
        expected=np.array([[-1, 1]], dtype=dtype))

    self._assertOpOutputMatchesExpected(
        array_ops.prevent_gradient,
        np.array([[-1, 1]], dtype=dtype),
        expected=np.array([[-1, 1]], dtype=dtype))

    self._assertOpOutputMatchesExpected(
        array_ops.squeeze,
        np.array([[[[[]]]]], dtype=dtype),
        expected=np.array([], dtype=dtype))
    self._assertOpOutputMatchesExpected(
        array_ops.squeeze,
        np.array([[[1], [2]]], dtype=dtype),
        expected=np.array([1, 2], dtype=dtype))
    self._assertOpOutputMatchesExpected(
        array_ops.squeeze,
        np.array([[[1]], [[2]]], dtype=dtype),
        expected=np.array([1, 2], dtype=dtype))
    self._assertOpOutputMatchesExpected(
        array_ops.squeeze,
        np.array([[[1, 2], [3, 4]]], dtype=dtype),
        expected=np.array([[1, 2], [3, 4]], dtype=dtype))

    self._assertOpOutputMatchesExpected(
        array_ops.stop_gradient,
        np.array([[-1, 1]], dtype=dtype),
        expected=np.array([[-1, 1]], dtype=dtype))
