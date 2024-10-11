# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_square_root_op_test.py
# The input to the square root should be at least a 2-dimensional tensor.
tensor = constant_op.constant([1., 2.])
with self.assertRaises((ValueError, errors_impl.InvalidArgumentError)):
    gen_linalg_ops.matrix_square_root(tensor)
