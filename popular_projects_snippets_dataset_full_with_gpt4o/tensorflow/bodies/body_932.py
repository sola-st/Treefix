# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/qr_op_test.py
dtype = x_np.dtype
shape = x_np.shape
with self.session() as sess:
    x_tf = array_ops.placeholder(dtype)
    with self.device_scope():
        q_tf, r_tf = linalg_ops.qr(x_tf, full_matrices=full_matrices)
    q_tf_val, r_tf_val = sess.run([q_tf, r_tf], feed_dict={x_tf: x_np})

    q_dims = q_tf_val.shape
    np_q = np.ndarray(q_dims, dtype)
    np_q_reshape = np.reshape(np_q, (-1, q_dims[-2], q_dims[-1]))
    new_first_dim = np_q_reshape.shape[0]

    x_reshape = np.reshape(x_np, (-1, x_np.shape[-2], x_np.shape[-1]))
    for i in range(new_first_dim):
        if full_matrices:
            np_q_reshape[i, :, :], _ = np.linalg.qr(
                x_reshape[i, :, :], mode="complete")
        else:
            np_q_reshape[i, :, :], _ = np.linalg.qr(
                x_reshape[i, :, :], mode="reduced")
    np_q = np.reshape(np_q_reshape, q_dims)
    if full_rank:
        # Q is unique up to sign/phase if the matrix is full-rank.
        self.CompareOrthogonal(np_q, q_tf_val, min(shape[-2:]))
    self.CheckApproximation(x_np, q_tf_val, r_tf_val)
    self.CheckUnitary(q_tf_val)
