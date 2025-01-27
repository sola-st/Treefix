# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/ternary_ops_test.py
for dtype in self.numeric_types:
    self._testTernary(
        array_ops.where_v2,
        np.array(False),
        np.array(2, dtype=dtype),
        np.array(7, dtype=dtype),
        expected=np.array(7, dtype=dtype))

    self._testTernary(
        array_ops.where_v2,
        np.array(True),
        np.array([1, 2, 3, 4], dtype=dtype),
        np.array([5, 6, 7, 8], dtype=dtype),
        expected=np.array([1, 2, 3, 4], dtype=dtype))

    self._testTernary(
        array_ops.where_v2,
        np.array(False),
        np.array([[1, 2], [3, 4], [5, 6]], dtype=dtype),
        np.array([[7, 8], [9, 10], [11, 12]], dtype=dtype),
        expected=np.array([[7, 8], [9, 10], [11, 12]], dtype=dtype))

    self._testTernary(
        array_ops.where_v2,
        np.array([0, 1, 1, 0], dtype=np.bool_),
        np.array([1, 2, 3, 4], dtype=dtype),
        np.array([5, 6, 7, 8], dtype=dtype),
        expected=np.array([5, 2, 3, 8], dtype=dtype))

    # Broadcast the condition
    self._testTernary(
        array_ops.where_v2,
        np.array([0, 1], dtype=np.bool_),
        np.array([[1, 2], [3, 4], [5, 6]], dtype=dtype),
        np.array([[7, 8], [9, 10], [11, 12]], dtype=dtype),
        expected=np.array([[7, 2], [9, 4], [11, 6]], dtype=dtype))

    # Broadcast the then branch to the else
    self._testTernary(
        array_ops.where_v2,
        np.array([[0, 1], [1, 0], [1, 1]], dtype=np.bool_),
        np.array([[1, 2]], dtype=dtype),
        np.array([[7, 8], [9, 10], [11, 12]], dtype=dtype),
        expected=np.array([[7, 2], [1, 10], [1, 2]], dtype=dtype))

    # Broadcast the else branch to the then
    self._testTernary(
        array_ops.where_v2,
        np.array([[1, 0], [0, 1], [0, 0]], dtype=np.bool_),
        np.array([[7, 8], [9, 10], [11, 12]], dtype=dtype),
        np.array([[1, 2]], dtype=dtype),
        expected=np.array([[7, 2], [1, 10], [1, 2]], dtype=dtype))

    # Broadcast the then/else branches to the condition
    self._testTernary(
        array_ops.where_v2,
        np.array([[1, 0], [0, 1], [1, 1]], dtype=np.bool_),
        np.array(7, dtype=dtype),
        np.array(8, dtype=dtype),
        expected=np.array([[7, 8], [8, 7], [7, 7]], dtype=dtype))
    self._testTernary(
        array_ops.where_v2,
        np.array([[1, 0], [0, 1], [0, 0]], dtype=np.bool_),
        np.array(7, dtype=dtype),
        np.array([8, 9], dtype=dtype),
        expected=np.array([[7, 9], [8, 7], [8, 9]], dtype=dtype))
