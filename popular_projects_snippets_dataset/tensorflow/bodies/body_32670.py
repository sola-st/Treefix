# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linalg_ops_test.py
x_ = np.array([
    [[1, 2], [3, 4]],
    [[7, 8], [3, 4]],
    [[0.25, 0.5], [0.75, -2.]],
],
              dtype=self.dtype)
x = array_ops.placeholder_with_default(
    x_, shape=x_.shape if self.use_static_shape else None)

y = linalg.lu_matrix_inverse(*linalg.lu(x), validate_args=True)
y_ = self.evaluate(y)

if self.use_static_shape:
    self.assertAllEqual(x_.shape, y.shape)
self.assertAllClose(np.linalg.inv(x_), y_, atol=0., rtol=1e-3)
