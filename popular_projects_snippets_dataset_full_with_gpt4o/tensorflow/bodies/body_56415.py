# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config_test.py
self._skip_if_tensor_float_32_unsupported()
self.assertTrue(config.tensor_float_32_execution_enabled())
config.enable_tensor_float_32_execution(False)
self.assertFalse(config.tensor_float_32_execution_enabled())

x = array_ops.fill((8, 8), 1 + 2**-20)
y = array_ops.ones((8, 8))
out = math_ops.matmul(x, y)
expected = array_ops.fill((8, 8), 8 * (1 + 2**-20))
self.assertAllEqual(out, expected)
