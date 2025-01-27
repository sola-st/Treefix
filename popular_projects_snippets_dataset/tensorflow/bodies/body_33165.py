# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_solve_op_test.py
if context.executing_eagerly():
    exit()
if test_util.is_xla_enabled() and self.pivoting:
    # Pivoting is not supported by xla backends.
    exit()
superdiag = array_ops.placeholder(dtypes.float64, shape=[None])
diag = array_ops.placeholder(dtypes.float64, shape=[None])
subdiag = array_ops.placeholder(dtypes.float64, shape=[None])
rhs = array_ops.placeholder(dtypes.float64, shape=[None])

x = linalg_impl.tridiagonal_solve((superdiag, diag, subdiag),
                                  rhs,
                                  diagonals_format="sequence",
                                  partial_pivoting=self.pivoting)
with self.cached_session() as sess:
    result = sess.run(
        x,
        feed_dict={
            subdiag: [20, 1, -1, 1],
            diag: [1, 3, 2, 2],
            superdiag: [2, 1, 4, 20],
            rhs: [1, 2, 3, 4]
        })
    self.assertAllClose(result, [-9, 5, -4, 4])
