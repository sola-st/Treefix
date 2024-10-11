# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/cholesky_op_test.py
for dtype in self.float_types:
    with self.assertRaises(ValueError):
        linalg_ops.cholesky(np.array([[1., 2., 3.], [3., 4., 5.]], dtype=dtype))
    with self.assertRaises(ValueError):
        linalg_ops.cholesky(
            np.array(
                [[[1., 2., 3.], [3., 4., 5.]], [[1., 2., 3.], [3., 4., 5.]]],
                dtype=dtype))
