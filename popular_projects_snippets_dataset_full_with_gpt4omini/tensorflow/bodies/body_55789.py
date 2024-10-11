# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tf2_test.py
self.assertTrue(tf2.enabled())
self.assertTrue(_pywrap_tf2.is_enabled())

v2_compat.enable_v2_behavior()
self.assertTrue(tf2.enabled())
self.assertTrue(_pywrap_tf2.is_enabled())

v2_compat.disable_v2_behavior()
self.assertFalse(tf2.enabled())
self.assertFalse(_pywrap_tf2.is_enabled())
