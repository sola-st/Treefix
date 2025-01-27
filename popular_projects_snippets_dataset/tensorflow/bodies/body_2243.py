# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/binary_ops_test.py
for dtype in self.float_types:
    rtol = 1e-14 if dtype == np.float64 else None

    self._testBinary(
        math_ops.pow, dtype(3), dtype(4), expected=dtype(81), rtol=rtol)

    self._testBinary(
        math_ops.pow,
        np.array([1, 2], dtype=dtype),
        np.zeros(shape=[0, 2], dtype=dtype),
        expected=np.zeros(shape=[0, 2], dtype=dtype),
        rtol=rtol)
    self._testBinary(
        math_ops.pow,
        np.array([10, 4], dtype=dtype),
        np.array([2, 3], dtype=dtype),
        expected=np.array([100, 64], dtype=dtype),
        rtol=rtol)
    self._testBinary(
        math_ops.pow,
        dtype(2),
        np.array([3, 4], dtype=dtype),
        expected=np.array([8, 16], dtype=dtype),
        rtol=rtol)
    self._testBinary(
        math_ops.pow,
        np.array([[2], [3]], dtype=dtype),
        dtype(4),
        expected=np.array([[16], [81]], dtype=dtype),
        rtol=rtol)
