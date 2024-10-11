# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linalg_ops_test.py
x_ = np.array([
    [[1, 2], [3, 4]],
    [[7, 8], [3, 4]],
    [[0.25, 0.5], [0.75, -2.]],
],
              dtype=self.dtype)
x = array_ops.placeholder_with_default(
    x_, shape=x_.shape if self.use_static_shape else None)
rhs_ = np.array([[1, 1]], dtype=self.dtype).T
rhs = array_ops.placeholder_with_default(
    rhs_, shape=rhs_.shape if self.use_static_shape else None)

lower_upper, perm = linalg.lu(x)
y = linalg.lu_solve(lower_upper, perm, rhs, validate_args=True)
y_, perm_ = self.evaluate([y, perm])

self.assertAllEqual([[1, 0], [0, 1], [1, 0]], perm_)
expected_ = np.linalg.solve(x_, rhs_[np.newaxis])
if self.use_static_shape:
    self.assertAllEqual(expected_.shape, y.shape)
self.assertAllClose(expected_, y_, atol=0., rtol=1e-3)
