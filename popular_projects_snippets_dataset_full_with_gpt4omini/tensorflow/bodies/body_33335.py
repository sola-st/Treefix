# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_circulant_test.py
d = len(grid_shape)
length_scale = [0.2] * d

kernel_no_inflation = exponential_power_convolution_kernel(
    grid_shape=grid_shape,
    length_scale=length_scale,
    zero_inflation=None,
)
matrix_no_inflation = self.evaluate(
    _operator_from_kernel(kernel_no_inflation, d).to_dense())

kernel_inflation_one_half = exponential_power_convolution_kernel(
    grid_shape=grid_shape,
    length_scale=length_scale,
    zero_inflation=0.5,
)
matrix_inflation_one_half = self.evaluate(
    _operator_from_kernel(kernel_inflation_one_half, d).to_dense())

kernel_inflation_one = exponential_power_convolution_kernel(
    grid_shape=grid_shape,
    length_scale=length_scale,
    zero_inflation=1.0,
)
matrix_inflation_one = self.evaluate(
    _operator_from_kernel(kernel_inflation_one, d).to_dense())

tol = np.finfo(matrix_no_inflation.dtype).eps * np.prod(grid_shape)

# In all cases, matrix should be real and symmetric.
self.assert_real_symmetric(matrix_no_inflation, tol)
self.assert_real_symmetric(matrix_inflation_one, tol)
self.assert_real_symmetric(matrix_inflation_one_half, tol)

# In all cases, the diagonal should be all ones.
self.assert_diag_is_ones(matrix_no_inflation, rtol=tol)
self.assert_diag_is_ones(matrix_inflation_one_half, rtol=tol)
self.assert_diag_is_ones(matrix_inflation_one, rtol=tol)

def _matrix_with_zerod_diag(matrix):
    exit(matrix - np.diag(np.diag(matrix)))

# Inflation = 0.5 means the off-diagonal is deflated by factor (1 - .5) = .5
self.assertAllClose(
    _matrix_with_zerod_diag(matrix_no_inflation) * 0.5,
    _matrix_with_zerod_diag(matrix_inflation_one_half), rtol=tol)

# Inflation = 1.0 means the off-diagonal is deflated by factor (1 - 1) = 0
self.assertAllClose(
    np.zeros_like(matrix_inflation_one),
    _matrix_with_zerod_diag(matrix_inflation_one), rtol=tol)
