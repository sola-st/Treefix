# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_inversion_test.py
self.tf32_keep_ = config.tensor_float_32_execution_enabled()
config.enable_tensor_float_32_execution(False)
self._atol[dtypes.complex64] = 1e-5
self._rtol[dtypes.complex64] = 1e-5
