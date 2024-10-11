# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tridiagonal_solve_ops_test.py
expected_grad_diags = np.array(expected_grad_diags).astype(np.float32)
expected_grad_rhs = np.array(expected_grad_rhs).astype(np.float32)
with self.session() as sess, self.test_scope():
    diags = _tfconst(diags)
    rhs = _tfconst(rhs)
    y = _tfconst(y)

    x = linalg_impl.tridiagonal_solve(
        diags,
        rhs,
        diagonals_format=diags_format,
        transpose_rhs=transpose_rhs,
        conjugate_rhs=False,
        partial_pivoting=False)

    res = math_ops.reduce_sum(x * y)
    actual_grad_diags = sess.run(
        gradient_ops.gradients(res, diags)[0], feed_dict=feed_dict)
    actual_rhs_diags = sess.run(
        gradient_ops.gradients(res, rhs)[0], feed_dict=feed_dict)
self.assertAllClose(expected_grad_diags, actual_grad_diags)
self.assertAllClose(expected_grad_rhs, actual_rhs_diags)
