# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/matrix_solve_op_test.py
for np_type in self.float_types & {np.float32, np.float64}:
    tol = 1e-4 if np_type == np.float32 else 1e-12
    a = x.astype(np_type)
    b = y.astype(np_type)
    np_ans = np.linalg.solve(np.swapaxes(a, -2, -1) if adjoint else a, b)
    with self.session() as sess:
        with self.test_scope():
            tf_ans = linalg_ops.matrix_solve(a, b, adjoint=adjoint)
        out = sess.run(tf_ans)
        self.assertEqual(tf_ans.shape, out.shape)
        self.assertEqual(np_ans.shape, out.shape)
        self.assertAllClose(np_ans, out, atol=tol, rtol=tol)
