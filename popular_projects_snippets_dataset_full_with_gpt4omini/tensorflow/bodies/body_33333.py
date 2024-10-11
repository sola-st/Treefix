# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_circulant_test.py
d = len(grid_shape)
length_scale = [0.2] * d
kernel = exponential_power_convolution_kernel(
    grid_shape=grid_shape,
    length_scale=length_scale,
    power=power)
operator = _operator_from_kernel(kernel, d)

matrix = self.evaluate(operator.to_dense())

tol = np.finfo(matrix.dtype).eps * np.prod(grid_shape)
self.assert_real_symmetric(matrix, tol)
self.assert_diag_is_ones(matrix, rtol=tol)
