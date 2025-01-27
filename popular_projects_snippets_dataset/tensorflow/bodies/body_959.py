# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/unary_ops_test.py
for dtype in self.float_types - {dtypes.bfloat16.as_numpy_dtype}:
    tol = 1e-4 if dtype == np.float32 else 1e-9
    # pylint: disable=invalid-unary-operand-type
    x = np.linspace(-np.e, np.e, num=1000, dtype=dtype)
    self._assertOpOutputMatchesExpected(
        math_ops.log, x, expected=np.log(x), atol=tol, rtol=tol)

    x = np.linspace(0., np.e * 1e-30, num=1000, dtype=dtype)
    self._assertOpOutputMatchesExpected(
        math_ops.log, x, expected=np.log(x), atol=tol, rtol=tol)

    x = np.linspace(0., np.pi * 1e30, num=1000, dtype=dtype)
    self._assertOpOutputMatchesExpected(
        math_ops.log, x, expected=np.log(x), atol=tol, rtol=tol)
