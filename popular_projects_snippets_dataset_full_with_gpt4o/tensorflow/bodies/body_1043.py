# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/einsum_op_test.py
for dtype in self.float_types:
    self._testUnary(
        lambda x: special_math_ops.einsum('ijk->kji', x),
        np.array([[[1, 3], [2, 5], [6, 8]]], dtype=dtype),
        expected=np.array([[[1], [2], [6]], [[3], [5], [8]]], dtype=dtype))
