# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_logarithm_op_test.py
# The input to the logarithm should be at least a 2-dimensional tensor.
tensor3 = constant_op.constant([1., 2.], dtype=dtypes.complex64)
with self.assertRaises((ValueError, errors_impl.InvalidArgumentError)):
    gen_linalg_ops.matrix_logarithm(tensor3)
