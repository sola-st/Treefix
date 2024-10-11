# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_inverse_op_test.py
# The input to the inverse should be at least a 2-dimensional tensor.
tensor3 = constant_op.constant([1., 2.])
with self.assertRaises(ValueError):
    linalg_ops.matrix_inverse(tensor3)
