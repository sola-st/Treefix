# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_exponential_op_test.py
# When the exponential of a non-square matrix is attempted we should return
# an error
with self.assertRaises(ValueError):
    linalg_impl.matrix_exponential(np.array([[1., 2., 3.], [3., 4., 5.]]))
