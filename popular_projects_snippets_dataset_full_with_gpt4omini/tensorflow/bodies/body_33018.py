# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/cholesky_op_test.py
tensor3 = constant_op.constant([1., 2.])
with self.assertRaises((ValueError, errors_impl.InvalidArgumentError)):
    linalg_ops.cholesky(tensor3)
with self.assertRaises((ValueError, errors_impl.InvalidArgumentError)):
    linalg_ops.cholesky(tensor3)
