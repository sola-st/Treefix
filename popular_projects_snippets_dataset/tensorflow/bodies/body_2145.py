# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/ternary_ops_test.py
# This operation is only supported for float32 and float64.
for dtype in self.numeric_types & {np.float32, np.float64}:
    # Randomly generate a, b, x in the numerical domain of betainc.
    # Compare against the implementation in SciPy.
    a = np.abs(np.random.randn(10, 10) * sigma).astype(dtype)  # in (0, infty)
    b = np.abs(np.random.randn(10, 10) * sigma).astype(dtype)  # in (0, infty)
    x = np.random.rand(10, 10).astype(dtype)  # in (0, 1)
    expected = sps.betainc(a, b, x, dtype=dtype)
    self._testTernary(
        math_ops.betainc, a, b, x, expected, rtol=rtol, atol=atol)
