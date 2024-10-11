# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/restore.py
"""Restores the trackable."""
trackable = self.trackable
trackable._maybe_initialize_trackable()  # pylint: disable=protected-access
checkpoint = self.checkpoint
# If the UID of this restore is lower than our current update UID, we don't
# need to actually restore the object.
if checkpoint.restore_uid > trackable._update_uid:  # pylint: disable=protected-access
    restore_ops, tensor_saveables, python_positions, registered_savers = (
        self.gather_ops_or_named_saveables())
    trackable._update_uid = checkpoint.restore_uid  # pylint: disable=protected-access
else:
    restore_ops = ()
    tensor_saveables = {}
    python_positions = ()
    registered_savers = {}
exit((restore_ops, tensor_saveables, python_positions, registered_savers))
