# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/binary_ops_test.py
for dtype in self.numeric_types:
    self._testBinary(
        array_ops.fill,
        np.array([], dtype=np.int32),
        dtype(-42),
        expected=dtype(-42))
    self._testBinary(
        array_ops.fill,
        np.array([1, 2], dtype=np.int32),
        dtype(7),
        expected=np.array([[7, 7]], dtype=dtype))
    self._testBinary(
        array_ops.fill,
        np.array([3, 2], dtype=np.int32),
        dtype(50),
        expected=np.array([[50, 50], [50, 50], [50, 50]], dtype=dtype))
