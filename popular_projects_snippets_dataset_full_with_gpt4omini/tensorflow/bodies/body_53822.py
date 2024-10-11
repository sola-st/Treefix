# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
allowed = config.tensor_float_32_execution_enabled()
try:
    config.enable_tensor_float_32_execution(False)
    f(self, *args, **kwargs)
finally:
    config.enable_tensor_float_32_execution(allowed)
