# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_test_util.py
with self.test_session(graph=ops.Graph()) as sess:
    # svd does not work with zero dimensional matrices, so we'll
    # skip
    if 0 in shapes_info.shape[-2:]:
        exit()

    # ROCm platform does not yet support complex types
    if test.is_built_with_rocm() and \
         ((dtype == dtypes.complex64) or (dtype == dtypes.complex128)):
        exit()

    sess.graph.seed = random_seed.DEFAULT_GRAPH_SEED
    # Ensure self-adjoint and PD so we get finite condition numbers.
    operator, mat = self.operator_and_matrix(
        shapes_info, dtype, use_placeholder=use_placeholder,
        ensure_self_adjoint_and_pd=True)
    # Eigenvalues are real, so we'll cast these to float64 and sort
    # for comparison.
    op_cond = operator.cond()
    s = math_ops.abs(linalg_ops.svd(mat, compute_uv=False))
    mat_cond = math_ops.reduce_max(s, axis=-1) / math_ops.reduce_min(
        s, axis=-1)
    op_cond_v, mat_cond_v = sess.run([op_cond, mat_cond])

    atol_override = {
        dtypes.float16: 1e-2,
        dtypes.float32: 1e-3,
        dtypes.float64: 1e-6,
        dtypes.complex64: 1e-3,
        dtypes.complex128: 1e-6,
    }
    rtol_override = {
        dtypes.float16: 1e-2,
        dtypes.float32: 1e-3,
        dtypes.float64: 1e-4,
        dtypes.complex64: 1e-3,
        dtypes.complex128: 1e-6,
    }
    atol = atol_override[dtype]
    rtol = rtol_override[dtype]
    self.assertAllClose(op_cond_v, mat_cond_v, atol=atol, rtol=rtol)
