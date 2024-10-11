# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/binary_ops_test.py
for dtype in self.float_types:
    self._testBinary(
        gen_math_ops.cross,
        np.zeros((4, 3), dtype=dtype),
        np.zeros((4, 3), dtype=dtype),
        expected=np.zeros((4, 3), dtype=dtype))
    self._testBinary(
        gen_math_ops.cross,
        np.array([1, 2, 3], dtype=dtype),
        np.array([4, 5, 6], dtype=dtype),
        expected=np.array([-3, 6, -3], dtype=dtype))
    self._testBinary(
        gen_math_ops.cross,
        np.array([[1, 2, 3], [10, 11, 12]], dtype=dtype),
        np.array([[4, 5, 6], [40, 50, 60]], dtype=dtype),
        expected=np.array([[-3, 6, -3], [60, -120, 60]], dtype=dtype))
