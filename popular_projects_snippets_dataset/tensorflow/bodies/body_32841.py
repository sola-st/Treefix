# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/svd_op_test.py
# The input to svd should be a tensor of at least rank 2.
scalar = constant_op.constant(1.)
with self.assertRaisesRegex((ValueError, errors_impl.InvalidArgumentError),
                            "rank.* 2.*0"):
    linalg_ops.svd(scalar)
vector = constant_op.constant([1., 2.])
with self.assertRaisesRegex((ValueError, errors_impl.InvalidArgumentError),
                            "rank.* 2.*1"):
    linalg_ops.svd(vector)
