# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/special_math_test.py
# Choose values outside the range where scipy float32 works.
# Let scipy use float64.  This means we
# won't be exactly the same since we are in float32.
self._test_grid_log(
    np.float32,  # dtype
    np.float64,  # scipy_dtype
    GridSpec(min=-50, max=self.CUTOFF_FLOAT32_UPPER + 5, shape=[100]),
    ErrorSpec(rtol=0.05, atol=0))
