# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/self_adjoint_eig_op_test.py

def CompareEigenVectors(self, x, y, tol):
    x = EquilibrateEigenVectorPhases(x, y)
    self.assertAllClose(x, y, atol=tol)

def CompareEigenDecompositions(self, x_e, x_v, y_e, y_v, tol):
    num_batches = int(np.prod(x_e.shape[:-1]))
    n = x_e.shape[-1]
    x_e = np.reshape(x_e, [num_batches] + [n])
    x_v = np.reshape(x_v, [num_batches] + [n, n])
    y_e = np.reshape(y_e, [num_batches] + [n])
    y_v = np.reshape(y_v, [num_batches] + [n, n])
    for i in range(num_batches):
        x_ei, x_vi = SortEigenDecomposition(x_e[i, :], x_v[i, :, :])
        y_ei, y_vi = SortEigenDecomposition(y_e[i, :], y_v[i, :, :])
        self.assertAllClose(x_ei, y_ei, atol=tol, rtol=tol)
        CompareEigenVectors(self, x_vi, y_vi, tol)

def Test(self):
    np.random.seed(1)
    n = shape_[-1]
    batch_shape = shape_[:-2]
    np_dtype = dtype_.as_numpy_dtype
    a = np.random.uniform(
        low=-1.0, high=1.0, size=n * n).reshape([n, n]).astype(np_dtype)
    if dtype_.is_complex:
        a += 1j * np.random.uniform(
            low=-1.0, high=1.0, size=n * n).reshape([n, n]).astype(np_dtype)
    a += np.conj(a.T)
    a = np.tile(a, batch_shape + (1, 1))
    if dtype_ in (dtypes_lib.float32, dtypes_lib.complex64):
        atol = 1e-4
    else:
        atol = 1e-12
    np_e, np_v = np.linalg.eigh(a)
    with self.session():
        if compute_v_:
            tf_e, tf_v = linalg_ops.self_adjoint_eig(constant_op.constant(a))

            # Check that V*diag(E)*V^T is close to A.
            a_ev = test_util.matmul_without_tf32(
                test_util.matmul_without_tf32(tf_v, array_ops.matrix_diag(tf_e)),
                tf_v,
                adjoint_b=True)
            self.assertAllClose(self.evaluate(a_ev), a, atol=atol)

            # Compare to numpy.linalg.eigh.
            CompareEigenDecompositions(self, np_e, np_v, self.evaluate(tf_e),
                                       self.evaluate(tf_v), atol)
        else:
            tf_e = linalg_ops.self_adjoint_eigvals(constant_op.constant(a))
            self.assertAllClose(
                np.sort(np_e, -1), np.sort(self.evaluate(tf_e), -1), atol=atol)

exit(Test)
