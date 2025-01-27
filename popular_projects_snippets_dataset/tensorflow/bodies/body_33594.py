# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/determinant_op_test.py
# When the determinant of a non-square matrix is attempted we should return
# an error
with self.assertRaises(ValueError):
    linalg_ops.matrix_determinant(
        np.array([[1., 2., 3.], [3., 5., 4.]]).astype(np.float32))
