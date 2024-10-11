# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_circulant_test.py
d = len(grid_shape)

kernel = exponential_power_convolution_kernel(
    grid_shape=grid_shape, length_scale=[0.001] * d, power=2)
matrix = self.evaluate(_operator_from_kernel(kernel, d).to_dense())

tol = np.finfo(matrix.dtype).eps * np.prod(grid_shape)
self.assertAllClose(matrix, np.eye(np.prod(grid_shape)), atol=tol)
self.assert_real_symmetric(matrix, tol)
