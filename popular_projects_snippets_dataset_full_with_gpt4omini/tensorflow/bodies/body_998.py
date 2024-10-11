# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/unary_ops_test.py
for dtype in self.float_types & {dtypes.float32, dtypes.float64}:
    self._assertSoftplusMatchesExpected([[-2, 0, 8]], dtype)
    self._assertSoftplusMatchesExpected(
        [[-9, 7, -5, 3, -1], [1, -3, 5, -7, 9]], dtype)
    if dtype == dtypes.bfloat16.as_numpy_dtype:
        log_eps = np.log(np.finfo(np.float32).eps)
    else:
        log_eps = np.log(np.finfo(dtype).eps)
    one = dtype(1)
    ten = dtype(10)
    self._assertSoftplusMatchesExpected([
        log_eps, log_eps - one, log_eps + one, log_eps - ten, log_eps + ten,
        -log_eps, -log_eps - one, -log_eps + one, -log_eps - ten,
        -log_eps + ten
    ], dtype)

    self._assertSoftplusMatchesExpected(
        [0.69302183, 0.69324386],
        dtype,
        equality_test=self.AssertCloseAndSorted,
        rtol=9e-5,
        atol=9e-5)
