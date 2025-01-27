# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/self_adjoint_eig_op_test.py
# The input to self_adjoint_eig should be a tensor of
# at least rank 2.
scalar = constant_op.constant(1.)
with self.assertRaises(ValueError):
    linalg_ops.self_adjoint_eig(scalar)
vector = constant_op.constant([1., 2.])
with self.assertRaises(ValueError):
    linalg_ops.self_adjoint_eig(vector)
