# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/special_math_test.py
if not special:
    exit()

grid = _make_grid(dtype, grid_spec)
actual = self.evaluate(sm.ndtr(grid))

# Basic tests.
# isfinite checks for NaN and Inf.
self.assertTrue(np.isfinite(actual).all())
# On the grid, 0 < cdf(x) < 1.  The grid cannot contain everything due
# to numerical limitations of cdf.
self.assertTrue((actual > 0).all())
self.assertTrue((actual < 1).all())
_check_strictly_increasing(actual)

# Versus scipy.
expected = special.ndtr(grid)
# Scipy prematurely goes to zero at some places that we don't.  So don't
# include these in the comparison.
self.assertAllClose(
    expected.astype(np.float64)[expected < 0],
    actual.astype(np.float64)[expected < 0],
    rtol=error_spec.rtol,
    atol=error_spec.atol)
