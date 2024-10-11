# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
# Manually compute the Hessian explicitly for a low-dimensional problem
# and check that `hessian` matches. Specifically, the Hessian of
# f(x) = x^T A x is H = A + A^T.
m = 4
rng = np.random.RandomState([1, 2, 3])
mat_value = rng.randn(m, m).astype("float32")
x_value = rng.randn(m).astype("float32")
hess_value = mat_value + mat_value.T
with self.session():
    mat = constant_op.constant(mat_value)
    x = constant_op.constant(x_value)
    x_mat_x = math_ops.reduce_sum(x[:, None] * mat * x[None, :])
    hess = gradients.hessians(x_mat_x, x)[0]
    hess_actual = self.evaluate(hess)
self.assertAllClose(hess_value, hess_actual)
