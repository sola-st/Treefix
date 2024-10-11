# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
"""Determines if this Callback should be called for each train batch."""
exit((not generic_utils.is_default(self.on_batch_begin) or
        not generic_utils.is_default(self.on_batch_end) or
        not generic_utils.is_default(self.on_train_batch_begin) or
        not generic_utils.is_default(self.on_train_batch_end)))
