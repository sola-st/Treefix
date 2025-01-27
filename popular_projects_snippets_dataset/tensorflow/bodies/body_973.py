# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/unary_ops_test.py
for dtype in self.numeric_types - {np.int8, np.uint8}:
    self._assertOpOutputMatchesExpected(
        math_ops.abs,
        np.array([[2, -1]], dtype=dtype),
        expected=np.array([[2, 1]], dtype=np.real(dtype(0)).dtype))

    self._assertOpOutputMatchesExpected(
        math_ops.negative,
        np.array([[-1, 1]], dtype=dtype),
        expected=np.array([[1, -1]], dtype=dtype))

    self._assertOpOutputMatchesExpected(
        math_ops.square,
        np.array([[-2, 3]], dtype=dtype),
        expected=np.array([[4, 9]], dtype=dtype))

    self._assertOpOutputMatchesExpected(
        array_ops.zeros_like,
        np.array([[4, 3], [2, 1]], dtype=dtype),
        expected=np.array([[0, 0], [0, 0]], dtype=dtype))

    self._assertOpOutputMatchesExpected(
        array_ops.ones_like,
        np.array([[4, 3], [2, 1]], dtype=dtype),
        expected=np.array([[1, 1], [1, 1]], dtype=dtype))
