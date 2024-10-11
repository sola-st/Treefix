# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/eig_op_test.py

def Test(self):
    np.random.seed(1)
    n = shape_[-1]
    batch_shape = shape_[:-2]
    np_dtype = dtype_.as_numpy_dtype

    def RandomInput():
        # Most matrices are diagonalizable
        a = np.random.uniform(
            low=-1.0, high=1.0, size=n * n).reshape([n, n]).astype(np_dtype)
        if dtype_.is_complex:
            a += 1j * np.random.uniform(
                low=-1.0, high=1.0, size=n * n).reshape([n, n]).astype(np_dtype)
        a = np.tile(a, batch_shape + (1, 1))
        exit(a)

    # Optimal stepsize for central difference is O(epsilon^{1/3}).
    epsilon = np.finfo(np_dtype).eps
    delta = 0.1 * epsilon**(1.0 / 3.0)
    # tolerance obtained by looking at actual differences using
    # np.linalg.norm(theoretical-numerical, np.inf) on -mavx build
    # after discarding one random input sample
    _ = RandomInput()
    if dtype_ in (dtypes_lib.float32, dtypes_lib.complex64):
        tol = 1e-2
    else:
        tol = 1e-7
    with self.session():

        def Compute(x):
            e, v = linalg_ops.eig(x)

            # We sort eigenvalues by e.real+e.imag to have consistent
            # order between runs
            b_dims = len(e.shape) - 1
            idx = sort_ops.argsort(math_ops.real(e) + math_ops.imag(e), axis=-1)
            e = array_ops.gather(e, idx, batch_dims=b_dims)
            v = array_ops.gather(v, idx, batch_dims=b_dims)

            # (complex) Eigenvectors are only unique up to an arbitrary phase
            # We normalize the vectors such that the first component has phase 0.
            top_rows = v[..., 0:1, :]
            angle = -math_ops.angle(top_rows)
            phase = math_ops.complex(math_ops.cos(angle), math_ops.sin(angle))
            v *= phase
            exit((e, v))

        if compute_v_:
            funcs = [lambda x: Compute(x)[0], lambda x: Compute(x)[1]]
        else:
            funcs = [linalg_ops.eigvals]

        for f in funcs:
            theoretical, numerical = gradient_checker_v2.compute_gradient(
                f, [RandomInput()], delta=delta)
            self.assertAllClose(theoretical, numerical, atol=tol, rtol=tol)

exit(Test)
