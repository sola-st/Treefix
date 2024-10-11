# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/qr_op_test.py
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
