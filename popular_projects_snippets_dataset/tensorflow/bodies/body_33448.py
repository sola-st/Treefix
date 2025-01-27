# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_low_rank_update_test.py
self.tf32_keep_ = config.tensor_float_32_execution_enabled()
config.enable_tensor_float_32_execution(False)
