# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_solve_op_test.py
for np_type in [np.float32, np.float64, np.complex64, np.complex128]:
    if np_type == np.float32 or np_type == np.complex64:
        tol = 1e-5
    else:
        tol = 1e-12
    for adjoint in False, True:
        if np_type in (np.float32, np.float64):
            a = x.real.astype(np_type)
            b = y.real.astype(np_type)
            a_np = np.transpose(a) if adjoint else a
        else:
            a = x.astype(np_type)
            b = y.astype(np_type)
            a_np = np.conj(np.transpose(a)) if adjoint else a
        if batch_dims is not None:
            a = np.tile(a, batch_dims + [1, 1])
            a_np = np.tile(a_np, batch_dims + [1, 1])
            b = np.tile(b, batch_dims + [1, 1])
        np_ans = np.linalg.solve(a_np, b)
        for use_placeholder in set((False, not context.executing_eagerly())):
            if use_placeholder:
                a_ph = array_ops.placeholder(dtypes.as_dtype(np_type))
                b_ph = array_ops.placeholder(dtypes.as_dtype(np_type))
                tf_ans = linalg_ops.matrix_solve(a_ph, b_ph, adjoint=adjoint)
                with self.cached_session() as sess:
                    out = sess.run(tf_ans, {a_ph: a, b_ph: b})
            else:
                tf_ans = linalg_ops.matrix_solve(a, b, adjoint=adjoint)
                out = self.evaluate(tf_ans)
                self.assertEqual(tf_ans.get_shape(), out.shape)
            self.assertEqual(np_ans.shape, out.shape)
            self.assertAllClose(np_ans, out, atol=tol, rtol=tol)
