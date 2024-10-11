# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_solve_ls_op_test.py
if not fast and l2_regularizer != 0:
    # The slow path does not support regularization.
    exit()
if use_placeholder and context.executing_eagerly():
    exit()
maxdim = np.max(x.shape)
if dtype == np.float32 or dtype == np.complex64:
    tol = maxdim * 5e-4
else:
    tol = maxdim * 5e-7
    a = x.astype(dtype)
    b = y.astype(dtype)
    if dtype in [np.complex64, np.complex128]:
        a.imag = a.real
        b.imag = b.real
    # numpy.linalg.lstqr does not batching, so we just solve a single system
    # and replicate the solution. and residual norm.
    np_ans = _SolveWithNumpy(x, y, l2_regularizer=l2_regularizer)
    np_r = np.dot(np.conj(a.T), b - np.dot(a, np_ans))
    np_r_norm = np.sqrt(np.sum(np.conj(np_r) * np_r))
    if batch_shape != ():
        a = np.tile(a, batch_shape + (1, 1))
        b = np.tile(b, batch_shape + (1, 1))
        np_ans = np.tile(np_ans, batch_shape + (1, 1))
        np_r_norm = np.tile(np_r_norm, batch_shape)
    if use_placeholder:
        a_ph = array_ops.placeholder(dtypes.as_dtype(dtype))
        b_ph = array_ops.placeholder(dtypes.as_dtype(dtype))
        feed_dict = {a_ph: a, b_ph: b}
        tf_ans = linalg_ops.matrix_solve_ls(
            a_ph, b_ph, fast=fast, l2_regularizer=l2_regularizer)
    else:
        tf_ans = linalg_ops.matrix_solve_ls(
            a, b, fast=fast, l2_regularizer=l2_regularizer)
        feed_dict = None
        self.assertEqual(np_ans.shape, tf_ans.get_shape())
    if feed_dict:
        with self.session() as sess:
            tf_ans_val = sess.run(tf_ans, feed_dict=feed_dict)
    else:
        tf_ans_val = self.evaluate(tf_ans)
    self.assertEqual(np_ans.shape, tf_ans_val.shape)
    self.assertAllClose(np_ans, tf_ans_val, atol=2 * tol, rtol=2 * tol)

    if l2_regularizer == 0:
        # The least squares solution should satisfy A^H * (b - A*x) = 0.
        tf_r = b - math_ops.matmul(a, tf_ans)
        tf_r = math_ops.matmul(a, tf_r, adjoint_a=True)
        tf_r_norm = linalg_ops.norm(tf_r, ord="fro", axis=[-2, -1])
        if feed_dict:
            with self.session() as sess:
                tf_ans_val, tf_r_norm_val = sess.run([tf_ans, tf_r_norm],
                                                     feed_dict=feed_dict)
        else:
            tf_ans_val, tf_r_norm_val = self.evaluate([tf_ans, tf_r_norm])
        self.assertAllClose(np_r_norm, tf_r_norm_val, atol=tol, rtol=tol)
