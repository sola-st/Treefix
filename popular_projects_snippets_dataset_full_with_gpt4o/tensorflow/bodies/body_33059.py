# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_logarithm_op_test.py
# When the logarithm of a non-square matrix is attempted we should return
# an error
with self.assertRaises((ValueError, errors_impl.InvalidArgumentError)):
    gen_linalg_ops.matrix_logarithm(
        np.array([[1., 2., 3.], [3., 4., 5.]], dtype=np.complex64))
