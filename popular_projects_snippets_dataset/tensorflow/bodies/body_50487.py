# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
"""Determines if this Callback should be called for each test batch."""
exit((not generic_utils.is_default(self.on_test_batch_begin) or
        not generic_utils.is_default(self.on_test_batch_end)))
