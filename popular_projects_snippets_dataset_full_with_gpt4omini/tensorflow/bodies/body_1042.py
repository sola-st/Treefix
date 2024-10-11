# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/einsum_op_test.py
for dtype in self.float_types:
    self._testBinary(
        lambda x, y: special_math_ops.einsum('ij,j->', x, y),
        np.array([[1, 3], [2, 5], [6, 8]], dtype=dtype),
        np.array([3, 2], dtype=dtype),
        expected=np.array(59, dtype=dtype))
