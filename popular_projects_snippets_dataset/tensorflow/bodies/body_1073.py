# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tridiagonal_solve_ops_test.py
np.random.seed(19)

batch_size = 8
num_dims = 11
num_rhs = 5

diagonals_np = np.random.normal(size=(batch_size, 3,
                                      num_dims)).astype(np.float32)
rhs_np = np.random.normal(size=(batch_size, num_dims,
                                num_rhs)).astype(np.float32)

with self.session() as sess, self.test_scope():
    diags = array_ops.placeholder(
        shape=(batch_size, 3, num_dims), dtype=dtypes.float32)
    rhs = array_ops.placeholder(
        shape=(batch_size, num_dims, num_rhs), dtype=dtypes.float32)
    x_np = sess.run(
        linalg_impl.tridiagonal_solve(diags, rhs, partial_pivoting=False),
        feed_dict={
            diags: diagonals_np,
            rhs: rhs_np
        })

superdiag_np = diagonals_np[:, 0]
diag_np = diagonals_np[:, 1]
subdiag_np = diagonals_np[:, 2]

for eq in range(num_rhs):
    y = np.zeros((batch_size, num_dims), dtype=np.float32)
    for i in range(num_dims):
        if i == 0:
            y[:, i] = (
                diag_np[:, i] * x_np[:, i, eq] +
                superdiag_np[:, i] * x_np[:, i + 1, eq])
        elif i == num_dims - 1:
            y[:, i] = (
                subdiag_np[:, i] * x_np[:, i - 1, eq] +
                diag_np[:, i] * x_np[:, i, eq])
        else:
            y[:, i] = (
                subdiag_np[:, i] * x_np[:, i - 1, eq] +
                diag_np[:, i] * x_np[:, i, eq] +
                superdiag_np[:, i] * x_np[:, i + 1, eq])

    self.assertAllClose(y, rhs_np[:, :, eq], rtol=1e-4, atol=1e-4)
