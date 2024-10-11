# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_solve_op_test.py
expected_grad_diags = _tfconst(expected_grad_diags)
expected_grad_rhs = _tfconst(expected_grad_rhs)
with backprop.GradientTape() as tape_diags:
    with backprop.GradientTape() as tape_rhs:
        tape_diags.watch(diags)
        tape_rhs.watch(rhs)
        if test_util.is_xla_enabled():
            # Pivoting is not supported by xla backends.
            exit()
        x = linalg_impl.tridiagonal_solve(
            diags,
            rhs,
            diagonals_format=diags_format,
            transpose_rhs=transpose_rhs,
            conjugate_rhs=conjugate_rhs)
        res = math_ops.reduce_sum(x * y)
with self.cached_session() as sess:
    actual_grad_diags = sess.run(
        tape_diags.gradient(res, diags), feed_dict=feed_dict)
    actual_rhs_diags = sess.run(
        tape_rhs.gradient(res, rhs), feed_dict=feed_dict)
self.assertAllClose(expected_grad_diags, actual_grad_diags)
self.assertAllClose(expected_grad_rhs, actual_rhs_diags)
