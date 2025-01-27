# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/binary_ops_test.py
for dtype in self.numeric_types:
    self._testBinary(
        array_ops.reshape,
        np.array([], dtype=dtype),
        np.array([0, 4], dtype=np.int32),
        expected=np.zeros(shape=[0, 4], dtype=dtype))
    self._testBinary(
        array_ops.reshape,
        np.array([0, 1, 2, 3, 4, 5], dtype=dtype),
        np.array([2, 3], dtype=np.int32),
        expected=np.array([[0, 1, 2], [3, 4, 5]], dtype=dtype))
    self._testBinary(
        array_ops.reshape,
        np.array([0, 1, 2, 3, 4, 5], dtype=dtype),
        np.array([3, 2], dtype=np.int32),
        expected=np.array([[0, 1], [2, 3], [4, 5]], dtype=dtype))
    self._testBinary(
        array_ops.reshape,
        np.array([0, 1, 2, 3, 4, 5], dtype=dtype),
        np.array([-1, 6], dtype=np.int32),
        expected=np.array([[0, 1, 2, 3, 4, 5]], dtype=dtype))
    self._testBinary(
        array_ops.reshape,
        np.array([0, 1, 2, 3, 4, 5], dtype=dtype),
        np.array([6, -1], dtype=np.int32),
        expected=np.array([[0], [1], [2], [3], [4], [5]], dtype=dtype))
    self._testBinary(
        array_ops.reshape,
        np.array([0, 1, 2, 3, 4, 5], dtype=dtype),
        np.array([2, -1], dtype=np.int32),
        expected=np.array([[0, 1, 2], [3, 4, 5]], dtype=dtype))
    self._testBinary(
        array_ops.reshape,
        np.array([0, 1, 2, 3, 4, 5], dtype=dtype),
        np.array([-1, 3], dtype=np.int32),
        expected=np.array([[0, 1, 2], [3, 4, 5]], dtype=dtype))
