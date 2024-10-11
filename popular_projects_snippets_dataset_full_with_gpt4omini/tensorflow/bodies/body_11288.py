# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_test_util.py
def test_eigvalsh(self):
    with self.test_session(graph=ops.Graph()) as sess:
        sess.graph.seed = random_seed.DEFAULT_GRAPH_SEED
        operator, mat = self.operator_and_matrix(
            shapes_info, dtype, use_placeholder=use_placeholder,
            ensure_self_adjoint_and_pd=True)
        # Eigenvalues are real, so we'll cast these to float64 and sort
        # for comparison.
        op_eigvals = sort_ops.sort(
            math_ops.cast(operator.eigvals(), dtype=dtypes.float64), axis=-1)
        if dtype.is_complex:
            mat = math_ops.cast(mat, dtype=dtypes.complex128)
        else:
            mat = math_ops.cast(mat, dtype=dtypes.float64)
        mat_eigvals = sort_ops.sort(
            math_ops.cast(
                linalg_ops.self_adjoint_eigvals(mat), dtype=dtypes.float64),
            axis=-1)
        op_eigvals_v, mat_eigvals_v = sess.run([op_eigvals, mat_eigvals])

        atol = self._atol[dtype]  # pylint: disable=protected-access
        rtol = self._rtol[dtype]  # pylint: disable=protected-access
        if dtype == dtypes.float32 or dtype == dtypes.complex64:
            atol = 2e-4
            rtol = 2e-4
        self.assertAllClose(op_eigvals_v, mat_eigvals_v, atol=atol, rtol=rtol)
exit(test_eigvalsh)
