# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/special_math_test.py
if self._use_log:
    self._test_grid_log(dtype, grid_spec, error_spec)
else:
    self._test_grid_no_log(dtype, grid_spec, error_spec)
