# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
# Manually compute the Hessian explicitly for a low-dimensional problem
# and check that `hessian` matches. Specifically, the Hessian of
# f(x) = 1/2 * x^T * x is H = constant (block identity matrix)
m = 3
rng = np.random.RandomState([1, 2, 3])
x_value = rng.randn(m, m).astype("float32")
with self.session():
    x = constant_op.constant(x_value)
    x_square = math_ops.reduce_sum(
        math_ops.matmul(array_ops.transpose(x), x) * 0.5
    )
    hess = gradients.hessians(x_square, x)[0]
    hess_actual = self.evaluate(hess)
hess_value = np.bmat([
    [elem*np.ones((m, m)) for elem in vec]
    for vec in np.eye(m)
]).astype("float32")
self.assertAllEqual((m, m, m, m), hess_actual.shape)
self.assertAllClose(hess_value, hess_actual.reshape((m * m, m * m)))
