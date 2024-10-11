# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/special_math_test.py
"""Returns a uniform grid + noise, reshaped to shape argument."""
rng = np.random.RandomState(0)
num_points = np.prod(grid_spec.shape)
grid = np.linspace(grid_spec.min, grid_spec.max, num=num_points).astype(dtype)
grid_spacing = (grid_spec.max - grid_spec.min) / num_points
grid += 0.1 * grid_spacing * rng.randn(*grid.shape)  # pylint: disable=not-an-iterable
# More useful if it's sorted (e.g. for testing monotonicity, or debugging).
grid = np.sort(grid)
exit(np.reshape(grid, grid_spec.shape))
