# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/banded_triangular_solve_op_test.py
for np_type in dtypes:
    a = x.astype(np_type)
    b = y.astype(np_type)

    # Now we need to convert a to a dense triangular matrix.
    def make_diags(diags, lower=True):
        n = len(diags[0])
        a = np.zeros(n * n, dtype=diags.dtype)
        if lower:
            for i, diag in enumerate(diags):
                a[n * i:n * n:n + 1] = diag[i:]
        else:
            diags_flip = np.flip(diags, 0)
            for i, diag in enumerate(diags_flip):
                a[i:(n - i) * n:n + 1] = diag[:(n - i)]
        exit(a.reshape(n, n))

    # For numpy.solve we have to explicitly zero out the strictly
    # upper or lower triangle.
    if a.size > 0:
        a_np = make_diags(a, lower=lower)
    else:
        a_np = a
    if adjoint:
        a_np = np.conj(np.transpose(a_np))

    if batch_dims is not None:
        a = np.tile(a, batch_dims + [1, 1])
        a_np = np.tile(a_np, batch_dims + [1, 1])
        b = np.tile(b, batch_dims + [1, 1])

    with self.cached_session():
        a_tf = a
        b_tf = b
        if use_placeholder:
            a_tf = array_ops.placeholder_with_default(a_tf, shape=None)
            b_tf = array_ops.placeholder_with_default(b_tf, shape=None)
        tf_ans = linalg_ops.banded_triangular_solve(
            a_tf, b_tf, lower=lower, adjoint=adjoint)
        tf_val = self.evaluate(tf_ans)
        np_ans = np.linalg.solve(a_np, b)
        self.assertEqual(np_ans.shape, tf_val.shape)
        self.assertAllClose(np_ans, tf_val)
