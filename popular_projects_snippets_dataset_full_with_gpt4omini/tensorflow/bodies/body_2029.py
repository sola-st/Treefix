# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/self_adjoint_eig_op_test.py
np.random.seed(1)
x_np = np.random.uniform(
    low=-1.0, high=1.0, size=np.prod(shape)).reshape(shape).astype(dtype)
x_np = x_np + np.swapaxes(x_np, -1, -2)
n = shape[-1]

e_np, _ = np.linalg.eigh(x_np)
with self.session() as sess:
    x_tf = array_ops.placeholder(dtype)
    with self.test_scope():
        e, v = linalg_ops.self_adjoint_eig(x_tf)
    e_val, v_val = sess.run([e, v], feed_dict={x_tf: x_np})

    v_diff = np.matmul(v_val, np.swapaxes(v_val, -1, -2)) - np.eye(n)
    self.assertAlmostEqual(np.mean(v_diff**2), 0.0, delta=1e-6)
    self.assertAlmostEqual(np.mean((e_val - e_np)**2), 0.0, delta=1e-6)
