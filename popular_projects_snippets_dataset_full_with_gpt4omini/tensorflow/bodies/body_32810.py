# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/qr_op_test.py
# The input to qr should be a tensor of at least rank 2.
scalar = constant_op.constant(1.)
with self.assertRaisesRegex((ValueError, errors_impl.InvalidArgumentError),
                            "rank.* 2.*0"):
    linalg_ops.qr(scalar)
vector = constant_op.constant([1., 2.])
with self.assertRaisesRegex((ValueError, errors_impl.InvalidArgumentError),
                            "rank.* 2.*1"):
    linalg_ops.qr(vector)
