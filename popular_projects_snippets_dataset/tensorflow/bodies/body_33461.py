# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/lu_op_test.py
# LU factorization gives an error when the input is singular.
# Note: A singular matrix may return without error but it won't be a valid
# factorization.
for dtype in self.float_types:
    with self.subTest(dtype=dtype):
        with self.assertRaises(errors.InvalidArgumentError):
            self.evaluate(
                linalg_ops.lu(
                    np.array([[1., 2., 3.], [2., 4., 6.], [2., 3., 4.]],
                             dtype=dtype)))
        with self.assertRaises(errors.InvalidArgumentError):
            self.evaluate(
                linalg_ops.lu(
                    np.array([[[1., 2., 3.], [2., 4., 6.], [1., 2., 3.]],
                              [[1., 2., 3.], [3., 4., 5.], [5., 6., 7.]]],
                             dtype=dtype)))
