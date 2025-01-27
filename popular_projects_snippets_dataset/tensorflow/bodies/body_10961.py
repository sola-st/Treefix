# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
m = 3
n = 4
rng = np.random.RandomState([1, 2, 3])
x_value = rng.randn(m, n).astype("float32")
with self.session():
    x = constant_op.constant(x_value)
    x_square = math_ops.reduce_sum(
        math_ops.matmul(array_ops.transpose(x), x) * 0.5
    )
    hess = gradients.hessians(x_square, x)[0]
    hess_actual = self.evaluate(hess)
hess_value = np.bmat([
    [elem*np.ones((n, n)) for elem in vec]
    for vec in np.eye(m)
]).astype("float32")
self.assertAllEqual((m, n, m, n), hess_actual.shape)
self.assertAllClose(hess_value, hess_actual.reshape((m * n, m * n)))
