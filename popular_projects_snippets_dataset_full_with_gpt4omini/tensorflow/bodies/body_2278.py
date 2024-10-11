# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/binary_ops_test.py
for dtype in self.numeric_types:
    self._testBinary(
        array_ops.tile,
        np.array([[6], [3], [4]], dtype=dtype),
        np.array([2, 0], dtype=np.int32),
        expected=np.empty([6, 0], dtype=dtype))
    self._testBinary(
        array_ops.tile,
        np.array([[6, 3, 4]], dtype=dtype),
        np.array([2, 0], dtype=np.int32),
        expected=np.empty([2, 0], dtype=dtype))
    self._testBinary(
        array_ops.tile,
        np.array([[6]], dtype=dtype),
        np.array([1, 2], dtype=np.int32),
        expected=np.array([[6, 6]], dtype=dtype))
    self._testBinary(
        array_ops.tile,
        np.array([[1], [2]], dtype=dtype),
        np.array([1, 2], dtype=np.int32),
        expected=np.array([[1, 1], [2, 2]], dtype=dtype))
    self._testBinary(
        array_ops.tile,
        np.array([[1, 2], [3, 4]], dtype=dtype),
        np.array([3, 2], dtype=np.int32),
        expected=np.array([[1, 2, 1, 2], [3, 4, 3, 4], [1, 2, 1, 2],
                           [3, 4, 3, 4], [1, 2, 1, 2], [3, 4, 3, 4]],
                          dtype=dtype))
    self._testBinary(
        array_ops.tile,
        np.array([[1, 2], [3, 4]], dtype=dtype),
        np.array([1, 1], dtype=np.int32),
        expected=np.array([[1, 2], [3, 4]], dtype=dtype))
    self._testBinary(
        array_ops.tile,
        np.array([[1, 2]], dtype=dtype),
        np.array([3, 1], dtype=np.int32),
        expected=np.array([[1, 2], [1, 2], [1, 2]], dtype=dtype))
