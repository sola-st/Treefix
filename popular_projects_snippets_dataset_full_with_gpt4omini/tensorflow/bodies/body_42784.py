# Extracted from ./data/repos/tensorflow/tensorflow/python/compat/disable_v2_behavior_test.py
t = constant_op.constant([1, 2, 3])  # creates a hidden context
self.assertTrue(isinstance(t, ops.EagerTensor))
t = _pywrap_tf2.is_enabled()
self.assertTrue(t)
v2_compat.disable_v2_behavior()
t = constant_op.constant([1, 2, 3])
self.assertFalse(isinstance(t, ops.EagerTensor))
t = _pywrap_tf2.is_enabled()
self.assertFalse(t)
