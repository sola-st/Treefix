# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/qr_op_test.py

is_complex = dtype_ in (np.complex64, np.complex128)
is_single = dtype_ in (np.float32, np.complex64)

def CompareOrthogonal(self, x, y, rank):
    if is_single:
        atol = 5e-4
    else:
        atol = 5e-14
    # We only compare the first 'rank' orthogonal vectors since the
    # remainder form an arbitrary orthonormal basis for the
    # (row- or column-) null space, whose exact value depends on
    # implementation details. Notice that since we check that the
    # matrices of singular vectors are unitary elsewhere, we do
    # implicitly test that the trailing vectors of x and y span the
    # same space.
    x = x[..., 0:rank]
    y = y[..., 0:rank]
    # Q is only unique up to sign (complex phase factor for complex matrices),
    # so we normalize the sign first.
    sum_of_ratios = np.sum(np.divide(y, x), -2, keepdims=True)
    phases = np.divide(sum_of_ratios, np.abs(sum_of_ratios))
    x *= phases
    self.assertAllClose(x, y, atol=atol)

def CheckApproximation(self, a, q, r):
    if is_single:
        tol = 1e-5
    else:
        tol = 1e-14
    # Tests that a ~= q*r.
    a_recon = test_util.matmul_without_tf32(q, r)
    self.assertAllClose(a_recon, a, rtol=tol, atol=tol)

def CheckUnitary(self, x):
    # Tests that x[...,:,:]^H * x[...,:,:] is close to the identity.
    xx = test_util.matmul_without_tf32(x, x, adjoint_a=True)
    identity = array_ops.matrix_band_part(array_ops.ones_like(xx), 0, 0)
    if is_single:
        tol = 1e-5
    else:
        tol = 1e-14
    self.assertAllClose(identity, xx, atol=tol)

@test_util.run_in_graph_and_eager_modes(use_gpu=True)
def Test(self):
    if not use_static_shape_ and context.executing_eagerly():
        exit()
    np.random.seed(1)
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
        q_tf, r_tf = linalg_ops.qr(x_tf, full_matrices=full_matrices_)

        if use_static_shape_:
            q_tf_val, r_tf_val = self.evaluate([q_tf, r_tf])
        else:
            with self.session() as sess:
                q_tf_val, r_tf_val = sess.run([q_tf, r_tf], feed_dict={x_tf: x_np})

        q_dims = q_tf_val.shape
        np_q = np.ndarray(q_dims, dtype_)
        np_q_reshape = np.reshape(np_q, (-1, q_dims[-2], q_dims[-1]))
        new_first_dim = np_q_reshape.shape[0]

        x_reshape = np.reshape(x_np, (-1, x_np.shape[-2], x_np.shape[-1]))
        for i in range(new_first_dim):
            if full_matrices_:
                np_q_reshape[i, :, :], _ = np.linalg.qr(
                    x_reshape[i, :, :], mode="complete")
            else:
                np_q_reshape[i, :, :], _ = np.linalg.qr(
                    x_reshape[i, :, :], mode="reduced")
        np_q = np.reshape(np_q_reshape, q_dims)
        CompareOrthogonal(self, np_q, q_tf_val, min(shape_[-2:]))
        CheckApproximation(self, x_np, q_tf_val, r_tf_val)
        CheckUnitary(self, q_tf_val)

exit(Test)
