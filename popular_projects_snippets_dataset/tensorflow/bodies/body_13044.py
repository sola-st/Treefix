# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
x_shape = [20, 7, 3]
for dtype in [np.complex64, np.complex128]:
    np.random.seed(1)
    x_np = (
        np.random.random_sample(x_shape).astype(dtype) +
        np.random.random_sample(x_shape).astype(dtype) * 1j)
    for dim in range(len(x_shape)):
        y_np = self._l2Normalize(x_np, dim)
        x_tf = constant_op.constant(x_np, name="x")
        y_tf = nn_impl.l2_normalize(x_tf, dim)
        self.assertAllClose(y_np, self.evaluate(y_tf))
