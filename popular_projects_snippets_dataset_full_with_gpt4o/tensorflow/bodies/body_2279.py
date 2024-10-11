# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/binary_ops_test.py
for dtype in self.numeric_types:
    self._testBinary(
        array_ops.transpose,
        np.zeros(shape=[1, 0, 4], dtype=dtype),
        np.array([1, 2, 0], dtype=np.int32),
        expected=np.zeros(shape=[0, 4, 1], dtype=dtype))
    self._testBinary(
        array_ops.transpose,
        np.array([[1, 2], [3, 4]], dtype=dtype),
        np.array([0, 1], dtype=np.int32),
        expected=np.array([[1, 2], [3, 4]], dtype=dtype))
    self._testBinary(
        array_ops.transpose,
        np.array([[1, 2], [3, 4]], dtype=dtype),
        np.array([1, 0], dtype=np.int32),
        expected=np.array([[1, 3], [2, 4]], dtype=dtype))
