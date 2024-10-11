# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/special_math_test.py
"""Verifies that ndtri computation is correct."""
if not special:
    exit()

p = np.linspace(0., 1.0, 50).astype(np.float64)
# Quantile performs piecewise rational approximation so adding some
# special input values to make sure we hit all the pieces.
p = np.hstack((p, np.exp(-32), 1. - np.exp(-32), np.exp(-2),
               1. - np.exp(-2)))
expected_x = special.ndtri(p)
x = special_math.ndtri(p)
self.assertAllClose(expected_x, self.evaluate(x), atol=0.)
