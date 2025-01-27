# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
for dtype in [dtypes.float32, dtypes.float64]:
    for shape in [(10, 10), (10, 9, 8), (100, 5, 5), (50, 40), (40, 50)]:
        init = init_ops.orthogonal_initializer(dtype=dtype)
        tol = 1e-5 if dtype == dtypes.float32 else 1e-12
        with self.session(graph=ops.Graph(), use_gpu=True):
            # Check the shape
            t = init(shape).eval()
            self.assertAllEqual(shape, t.shape)
            # Check orthogonality by computing the inner product
            t = t.reshape((np.prod(t.shape[:-1]), t.shape[-1]))
            if t.shape[0] > t.shape[1]:
                self.assertAllClose(
                    np.dot(t.T, t), np.eye(t.shape[1]), rtol=tol, atol=tol)
            else:
                self.assertAllClose(
                    np.dot(t, t.T), np.eye(t.shape[0]), rtol=tol, atol=tol)
