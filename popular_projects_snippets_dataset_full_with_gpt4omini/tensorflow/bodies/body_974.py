# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/unary_ops_test.py
for dtype in self.float_types:
    self._assertOpOutputMatchesExpected(
        math_ops.is_inf,
        np.array([[np.NINF, -2, -1, 0, 0.5, 1, 2, np.inf, np.nan]],
                 dtype=dtype),
        expected=np.array([[1, 0, 0, 0, 0, 0, 0, 1, 0]], dtype=np.bool_))
    self._assertOpOutputMatchesExpected(
        math_ops.is_nan,
        np.array([[np.NINF, -2, -1, 0, 0.5, 1, 2, np.inf, np.nan]],
                 dtype=dtype),
        expected=np.array([[0, 0, 0, 0, 0, 0, 0, 0, 1]], dtype=np.bool_))
    self._assertOpOutputMatchesExpected(
        math_ops.sign,
        np.array([[np.nan]], dtype=dtype),
        expected=np.array([[0.0]], dtype=dtype))
