# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_inverse_op_test.py
# When the inverse of a non-square matrix is attempted we should return
# an error
with self.assertRaises(ValueError):
    linalg_ops.matrix_inverse(np.array([[1., 2., 3.], [3., 4., 5.]]))
