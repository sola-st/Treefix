# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/unary_ops_test.py
for dtype in self.float_types - {dtypes.bfloat16.as_numpy_dtype}:
    tol = 1e-6 if dtype == np.float32 else 1e-12

    x = np.linspace(-4 * np.e, 4 * np.e, num=1000, dtype=dtype)
    self._assertOpOutputMatchesExpected(
        math_ops.sin, x, expected=np.sin(x), rtol=tol, atol=tol)

    x = np.linspace(0., np.e * 1e-30, num=1000, dtype=dtype)
    self._assertOpOutputMatchesExpected(
        math_ops.sin, x, expected=np.sin(x), rtol=tol, atol=tol)

    if dtype == np.float64:
        x = np.linspace(0., np.e * 1e8, num=1000, dtype=dtype)
        self._assertOpOutputMatchesExpected(
            math_ops.sin, x, expected=np.sin(x), rtol=tol, atol=1e-5)
