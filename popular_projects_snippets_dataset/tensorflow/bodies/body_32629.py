# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_inverse_op_test.py
# The input should be invertible.
with self.cached_session():
    with self.assertRaisesOpError("Input is not invertible."):
        # All rows of the matrix below add to zero.
        tensor3 = constant_op.constant([[1., 0., -1.], [-1., 1., 0.],
                                        [0., -1., 1.]])
        linalg_ops.matrix_inverse(tensor3).eval()
