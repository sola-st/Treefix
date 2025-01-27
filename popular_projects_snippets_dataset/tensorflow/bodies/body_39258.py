# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/restore.py
"""Restore this value into `trackable`."""
with ops.init_scope():
    if self.bind_object(trackable):
        # This object's correspondence with a checkpointed object is new, so
        # process deferred restorations for it and its dependencies.
        restore_ops = self._restore_descendants(reader)
        if restore_ops:
            self._checkpoint.new_restore_ops(restore_ops)
