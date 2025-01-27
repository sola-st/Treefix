# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_low_rank_update_test.py
self.tf32_keep_ = config.tensor_float_32_execution_enabled()
config.enable_tensor_float_32_execution(False)
# Decrease tolerance since we are testing with condition numbers as high as
# 1e4.
self._atol[dtypes.float32] = 1e-5
self._rtol[dtypes.float32] = 1e-5
self._atol[dtypes.float64] = 1e-10
self._rtol[dtypes.float64] = 1e-10
self._rtol[dtypes.complex64] = 1e-4
