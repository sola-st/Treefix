# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config_test.py
self.assertTrue(config.tensor_float_32_execution_enabled())
self.assertTrue(test_ops.is_tensor_float32_enabled())
config.enable_tensor_float_32_execution(False)
self.assertFalse(config.tensor_float_32_execution_enabled())
self.assertFalse(test_ops.is_tensor_float32_enabled())
config.enable_tensor_float_32_execution(True)
self.assertTrue(config.tensor_float_32_execution_enabled())
self.assertTrue(test_ops.is_tensor_float32_enabled())
