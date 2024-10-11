# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/subscribe_test.py
"""Confirm subscribed identity ops are correctly detected."""
a = constant_op.constant(1)
b = constant_op.constant(2)
c = math_ops.add(a, b)
idop = array_ops.identity(c)
c_sub = subscribe.subscribe(c, [])

self.assertFalse(subscribe._is_subscribed_identity(a))
self.assertFalse(subscribe._is_subscribed_identity(c))
self.assertFalse(subscribe._is_subscribed_identity(idop))
self.assertTrue(subscribe._is_subscribed_identity(c_sub))
