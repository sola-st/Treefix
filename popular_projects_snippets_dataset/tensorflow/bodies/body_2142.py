# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/ternary_ops_test.py
for dtype in self.numeric_types:
    self._testTernary(
        array_ops.slice,
        np.array([[], [], []], dtype=dtype),
        np.array([1, 0], dtype=np.int32),
        np.array([2, 0], dtype=np.int32),
        expected=np.array([[], []], dtype=dtype))

    self._testTernary(
        array_ops.slice,
        np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=dtype),
        np.array([0, 1], dtype=np.int32),
        np.array([2, 1], dtype=np.int32),
        expected=np.array([[2], [5]], dtype=dtype))
