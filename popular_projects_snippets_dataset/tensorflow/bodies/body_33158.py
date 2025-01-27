# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_solve_op_test.py
if context.executing_eagerly():
    exit()
diags = array_ops.placeholder(dtypes.float64, shape=diags_shape)
rhs = array_ops.placeholder(dtypes.float64, shape=rhs_shape)
if test_util.is_xla_enabled() and self.pivoting:
    # Pivoting is not supported by xla backends.
    exit()
x = linalg_impl.tridiagonal_solve(
    diags, rhs, diags_format, partial_pivoting=self.pivoting)
with self.cached_session() as sess:
    result = sess.run(x, feed_dict={diags: diags_feed, rhs: rhs_feed})
    self.assertAllClose(result, expected)
