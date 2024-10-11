# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/ternary_ops_test.py
# This operation is only supported for float32 and float64.
for dtype in self.numeric_types & {np.float32, np.float64}:
    # Sanity check a few identities:
    # - betainc(a, b, 0) == 0
    # - betainc(a, b, 1) == 1
    # - betainc(a, 1, x) == x ** a
    # Compare against the implementation in SciPy.
    a = np.array([.3, .4, .2, .2], dtype=dtype)
    b = np.array([1., 1., .4, .4], dtype=dtype)
    x = np.array([.3, .4, .0, .1], dtype=dtype)
    expected = sps.betainc(a, b, x)
    self._testTernary(
        math_ops.betainc, a, b, x, expected, rtol=5e-6, atol=6e-6)
