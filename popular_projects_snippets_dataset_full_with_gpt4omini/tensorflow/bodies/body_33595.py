# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/determinant_op_test.py
# The input to the determinant should be a 2-dimensional tensor.
tensor1 = constant_op.constant([1., 2.])
with self.assertRaises(ValueError):
    linalg_ops.matrix_determinant(tensor1)
