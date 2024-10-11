# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/cholesky_op_test.py
with self.assertRaises((ValueError, errors_impl.InvalidArgumentError)):
    linalg_ops.cholesky(np.array([[1., 2., 3.], [3., 4., 5.]]))
with self.assertRaises((ValueError, errors_impl.InvalidArgumentError)):
    linalg_ops.cholesky(
        np.array([[[1., 2., 3.], [3., 4., 5.]], [[1., 2., 3.], [3., 4., 5.]]
                 ]))
