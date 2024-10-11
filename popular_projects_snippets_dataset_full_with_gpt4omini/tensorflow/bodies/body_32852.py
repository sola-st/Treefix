# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/svd_op_test.py

def CompareSingularValues(self, x, y, tol):
    atol = (x[0] + y[0]) * tol if len(x) else tol
    self.assertAllClose(x, y, atol=atol)

def CompareSingularVectors(self, x, y, rank, tol):
    # We only compare the first 'rank' singular vectors since the
    # remainder form an arbitrary orthonormal basis for the
    # (row- or column-) null space, whose exact value depends on
    # implementation details. Notice that since we check that the
    # matrices of singular vectors are unitary elsewhere, we do
    # implicitly test that the trailing vectors of x and y span the
    # same space.
    x = x[..., 0:rank]
    y = y[..., 0:rank]
    # Singular vectors are only unique up to sign (complex phase factor for
    # complex matrices), so we normalize the sign first.
    sum_of_ratios = np.sum(np.divide(y, x), -2, keepdims=True)
    phases = np.divide(sum_of_ratios, np.abs(sum_of_ratios))
    x *= phases
    self.assertAllClose(x, y, atol=2 * tol)

def CheckApproximation(self, a, u, s, v, full_matrices_, tol):
    # Tests that a ~= u*diag(s)*transpose(v).
    batch_shape = a.shape[:-2]
    m = a.shape[-2]
    n = a.shape[-1]
    diag_s = math_ops.cast(array_ops.matrix_diag(s), dtype=dtype_)
    if full_matrices_:
        if m > n:
            zeros = array_ops.zeros(batch_shape + (m - n, n), dtype=dtype_)
            diag_s = array_ops.concat([diag_s, zeros], a.ndim - 2)
        elif n > m:
            zeros = array_ops.zeros(batch_shape + (m, n - m), dtype=dtype_)
            diag_s = array_ops.concat([diag_s, zeros], a.ndim - 1)
    a_recon = math_ops.matmul(u, diag_s)
    a_recon = math_ops.matmul(a_recon, v, adjoint_b=True)
    self.assertAllClose(a_recon, a, rtol=tol, atol=tol)

def CheckUnitary(self, x, tol):
    # Tests that x[...,:,:]^H * x[...,:,:] is close to the identity.
    xx = math_ops.matmul(x, x, adjoint_a=True)
    identity = array_ops.matrix_band_part(array_ops.ones_like(xx), 0, 0)
    self.assertAllClose(identity, xx, atol=tol)

@test_util.run_in_graph_and_eager_modes(use_gpu=True)
def Test(self):
    if not use_static_shape_ and context.executing_eagerly():
        exit()
    is_complex = dtype_ in (np.complex64, np.complex128)
    is_single = dtype_ in (np.float32, np.complex64)
    tol = 3e-4 if is_single else 1e-12
    if test.is_gpu_available():
        # The gpu version returns results that are much less accurate.
        tol *= 200
    np.random.seed(42)
    x_np = np.random.uniform(
        low=-1.0, high=1.0, size=np.prod(shape_)).reshape(shape_).astype(dtype_)
    if is_complex:
        x_np += 1j * np.random.uniform(
            low=-1.0, high=1.0,
            size=np.prod(shape_)).reshape(shape_).astype(dtype_)

    if use_static_shape_:
        x_tf = constant_op.constant(x_np)
    else:
        x_tf = array_ops.placeholder(dtype_)

    if compute_uv_:
        s_tf, u_tf, v_tf = linalg_ops.svd(
            x_tf, compute_uv=compute_uv_, full_matrices=full_matrices_)
        if use_static_shape_:
            s_tf_val, u_tf_val, v_tf_val = self.evaluate([s_tf, u_tf, v_tf])
        else:
            with self.session() as sess:
                s_tf_val, u_tf_val, v_tf_val = sess.run([s_tf, u_tf, v_tf],
                                                        feed_dict={x_tf: x_np})
    else:
        s_tf = linalg_ops.svd(
            x_tf, compute_uv=compute_uv_, full_matrices=full_matrices_)
        if use_static_shape_:
            s_tf_val = self.evaluate(s_tf)
        else:
            with self.session() as sess:
                s_tf_val = sess.run(s_tf, feed_dict={x_tf: x_np})

    if compute_uv_:
        u_np, s_np, v_np = np.linalg.svd(
            x_np, compute_uv=compute_uv_, full_matrices=full_matrices_)
    else:
        s_np = np.linalg.svd(
            x_np, compute_uv=compute_uv_, full_matrices=full_matrices_)
    # We explicitly avoid the situation where numpy eliminates a first
    # dimension that is equal to one.
    s_np = np.reshape(s_np, s_tf_val.shape)

    CompareSingularValues(self, s_np, s_tf_val, tol)
    if compute_uv_:
        CompareSingularVectors(self, u_np, u_tf_val, min(shape_[-2:]), tol)
        CompareSingularVectors(self, np.conj(np.swapaxes(v_np, -2, -1)), v_tf_val,
                               min(shape_[-2:]), tol)
        CheckApproximation(self, x_np, u_tf_val, s_tf_val, v_tf_val,
                           full_matrices_, tol)
        CheckUnitary(self, u_tf_val, tol)
        CheckUnitary(self, v_tf_val, tol)

exit(Test)
