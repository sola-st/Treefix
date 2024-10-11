# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/einsum_op_test.py
for dtype in self.float_types:
    self._testBinary(
        lambda x, y: special_math_ops.einsum('ij,jk->ik', x, y),
        np.array([[-0.25]], dtype=dtype),
        np.array([[8]], dtype=dtype),
        expected=np.array([[-2]], dtype=dtype))
