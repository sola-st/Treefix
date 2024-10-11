# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2_test.py
for shape in [(10, 10), (10, 9, 8), (100, 5, 5), (50, 40), (40, 50)]:
    init = init_ops_v2.Orthogonal()
    tol = 1e-5
    with test_util.use_gpu():
        # Check the shape
        t = self.evaluate(init(shape))
        self.assertAllEqual(shape, t.shape)
        # Check orthogonality by computing the inner product
        t = t.reshape((np.prod(t.shape[:-1]), t.shape[-1]))
        if t.shape[0] > t.shape[1]:
            self.assertAllClose(
                np.dot(t.T, t), np.eye(t.shape[1]), rtol=tol, atol=tol)
        else:
            self.assertAllClose(
                np.dot(t, t.T), np.eye(t.shape[0]), rtol=tol, atol=tol)
