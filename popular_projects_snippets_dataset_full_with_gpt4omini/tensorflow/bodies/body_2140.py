# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/ternary_ops_test.py
for dtype in self.numeric_types:
    self._testTernary(
        array_ops.where,
        np.array(False),
        np.array(2, dtype=dtype),
        np.array(7, dtype=dtype),
        expected=np.array(7, dtype=dtype))

    self._testTernary(
        array_ops.where,
        np.array(True),
        np.array([1, 2, 3, 4], dtype=dtype),
        np.array([5, 6, 7, 8], dtype=dtype),
        expected=np.array([1, 2, 3, 4], dtype=dtype))

    self._testTernary(
        array_ops.where,
        np.array(False),
        np.array([[1, 2], [3, 4], [5, 6]], dtype=dtype),
        np.array([[7, 8], [9, 10], [11, 12]], dtype=dtype),
        expected=np.array([[7, 8], [9, 10], [11, 12]], dtype=dtype))

    self._testTernary(
        array_ops.where,
        np.array([0, 1, 1, 0], dtype=np.bool_),
        np.array([1, 2, 3, 4], dtype=dtype),
        np.array([5, 6, 7, 8], dtype=dtype),
        expected=np.array([5, 2, 3, 8], dtype=dtype))

    self._testTernary(
        array_ops.where,
        np.array([0, 1, 0], dtype=np.bool_),
        np.array([[1, 2], [3, 4], [5, 6]], dtype=dtype),
        np.array([[7, 8], [9, 10], [11, 12]], dtype=dtype),
        expected=np.array([[7, 8], [3, 4], [11, 12]], dtype=dtype))
