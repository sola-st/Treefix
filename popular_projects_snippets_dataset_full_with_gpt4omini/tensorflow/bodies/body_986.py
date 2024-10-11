# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/unary_ops_test.py
shape_op = lambda x: array_ops.shape_internal(x, optimize=False)
for dtype in self.numeric_types:
    self._assertOpOutputMatchesExpected(
        shape_op, dtype(7), expected=np.array([], dtype=np.int32))
    self._assertOpOutputMatchesExpected(
        shape_op,
        np.array([[], []], dtype=dtype),
        expected=np.array([2, 0], dtype=np.int32))
    self._assertOpOutputMatchesExpected(
        shape_op,
        np.array([-1, 1], dtype=dtype),
        expected=np.array([2], dtype=np.int32))
    self._assertOpOutputMatchesExpected(
        shape_op,
        np.array([[-1, 1]], dtype=dtype),
        expected=np.array([1, 2], dtype=np.int32))
    self._assertOpOutputMatchesExpected(
        shape_op,
        np.array([[-1], [1], [4]], dtype=dtype),
        expected=np.array([3, 1], dtype=np.int32))
