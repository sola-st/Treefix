# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/binary_ops_test.py
for dtype in self.complex_types:
    self._testBinary(
        array_ops.conjugate_transpose,
        np.zeros(shape=[1, 0, 4], dtype=dtype),
        np.array([1, 2, 0], dtype=np.int32),
        expected=np.zeros(shape=[0, 4, 1], dtype=dtype))
    self._testBinary(
        array_ops.conjugate_transpose,
        np.array([[1 - 1j, 2 + 2j], [3 - 3j, 4 + 4j]], dtype=dtype),
        np.array([0, 1], dtype=np.int32),
        expected=np.array([[1 + 1j, 2 - 2j], [3 + 3j, 4 - 4j]], dtype=dtype))
    self._testBinary(
        array_ops.conjugate_transpose,
        np.array([[1 - 1j, 2 + 2j], [3 - 3j, 4 + 4j]], dtype=dtype),
        np.array([1, 0], dtype=np.int32),
        expected=np.array([[1 + 1j, 3 + 3j], [2 - 2j, 4 - 4j]], dtype=dtype))
