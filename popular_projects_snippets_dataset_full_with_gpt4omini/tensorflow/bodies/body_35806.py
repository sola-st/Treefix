# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variables_test.py
with self.cached_session():
    var = variables.Variable(2.0)
    self.assertEqual(var.device, var.initialized_value().device)

    var_cached = variables.Variable(2.0, caching_device="/job:foo")
    self.assertFalse(var_cached.device.startswith("/job:foo"))
    self.assertTrue(var_cached.value().device.startswith("/job:foo"))
