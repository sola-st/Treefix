# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_exponential_op_test.py
# The input to the exponential should be at least a 2-dimensional tensor.
tensor3 = constant_op.constant([1., 2.])
with self.assertRaises(ValueError):
    linalg_impl.matrix_exponential(tensor3)
