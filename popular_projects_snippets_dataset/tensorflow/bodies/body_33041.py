# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_kronecker_test.py
self.tf32_keep_ = config.tensor_float_32_execution_enabled()
config.enable_tensor_float_32_execution(False)
# Increase from 1e-6 to 1e-4
self._atol[dtypes.float32] = 1e-4
self._atol[dtypes.complex64] = 1e-4
self._rtol[dtypes.float32] = 1e-4
self._rtol[dtypes.complex64] = 1e-4
