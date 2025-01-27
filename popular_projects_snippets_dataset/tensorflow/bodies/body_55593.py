# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/subscribe_test.py
"""Convenience function to test a container of subscribed identities."""
self.assertTrue(
    all(subscribe._is_subscribed_identity(x) for x in container))
