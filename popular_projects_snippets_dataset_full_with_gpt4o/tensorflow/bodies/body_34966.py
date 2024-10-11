# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/special_math_test.py
# Choose values mild enough that we can use scipy in float32, which will
# allow for a high accuracy match to scipy (since we both use float32).
self._test_grid_log(
    np.float32,  # dtype
    np.float32,  # scipy_dtype
    GridSpec(min=-10, max=self.CUTOFF_FLOAT32_UPPER - 5, shape=[100]),
    ErrorSpec(rtol=5e-4, atol=0))
