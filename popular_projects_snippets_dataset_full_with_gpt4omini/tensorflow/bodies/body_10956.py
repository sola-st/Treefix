# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
# Manually compute the Hessian explicitly for a low-dimensional problem
# and check that HessianVectorProduct matches multiplication by the
# explicit Hessian.
# Specifically, the Hessian of f(x) = x^T A x is
# H = A + A^T.
# We expect HessianVectorProduct(f(x), x, v) to be H v.
m = 4
rng = np.random.RandomState([1, 2, 3])
mat_value = rng.randn(m, m).astype("float32")
v_value = rng.randn(m, 1).astype("float32")
x_value = rng.randn(m, 1).astype("float32")
hess_value = mat_value + mat_value.T
hess_v_value = np.dot(hess_value, v_value)
for use_gpu in [False, True]:
    with self.cached_session(use_gpu=use_gpu):
        mat = constant_op.constant(mat_value)
        v = constant_op.constant(v_value)
        x = constant_op.constant(x_value)
        mat_x = math_ops.matmul(mat, x, name="Ax")
        x_mat_x = math_ops.matmul(array_ops.transpose(x), mat_x, name="xAx")
        hess_v = gradients_impl._hessian_vector_product(x_mat_x, [x], [v])[0]
        hess_v_actual = self.evaluate(hess_v)
    self.assertAllClose(hess_v_value, hess_v_actual)
