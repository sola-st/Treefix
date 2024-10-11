# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tridiagonal_solve_ops_test.py
np.random.seed(0)
batch_size = 8
num_dims = 11
num_rhs = 5

diagonals_np = np.random.normal(size=(batch_size, 3,
                                      num_dims)).astype(np.float32)
rhs_np = np.random.normal(size=(batch_size, num_dims,
                                num_rhs)).astype(np.float32)

with self.session() as sess, self.test_scope():
    with self.assertRaisesRegex(
        errors_impl.UnimplementedError,
        "Current implementation does not yet support pivoting."):
        diags = array_ops.placeholder(
            shape=(batch_size, 3, num_dims), dtype=dtypes.float32)
        rhs = array_ops.placeholder(
            shape=(batch_size, num_dims, num_rhs), dtype=dtypes.float32)
        sess.run(
            linalg_impl.tridiagonal_solve(diags, rhs, partial_pivoting=True),
            feed_dict={
                diags: diagonals_np,
                rhs: rhs_np
            })
