# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/cholesky_op_test.py
for dtype in self.float_types:
    tensor3 = constant_op.constant([1., 2.], dtype=dtype)
    with self.assertRaises(ValueError):
        linalg_ops.cholesky(tensor3)
    with self.assertRaises(ValueError):
        linalg_ops.cholesky(tensor3)
