# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/unary_ops_test.py
size_op = lambda x: array_ops.size_internal(x, optimize=False)
for dtype in self.numeric_types:
    self._assertOpOutputMatchesExpected(
        size_op, dtype(7), expected=np.int32(1))
    self._assertOpOutputMatchesExpected(
        size_op, np.array([[], []], dtype=dtype), expected=np.int32(0))
    self._assertOpOutputMatchesExpected(
        size_op, np.array([-1, 1], dtype=dtype), expected=np.int32(2))
    self._assertOpOutputMatchesExpected(
        size_op, np.array([[-1, 1]], dtype=dtype), expected=np.int32(2))
    self._assertOpOutputMatchesExpected(
        size_op,
        np.array([[-1], [1], [4]], dtype=dtype),
        expected=np.int32(3))
