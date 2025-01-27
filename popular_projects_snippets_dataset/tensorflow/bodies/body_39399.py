# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_management.py
timestamp = time.time()
# If this is an overwritten checkpoint we were previously tracking, delete
# and reinsert it to make sure it goes to the end of the queue.
if save_path in self._maybe_delete:
    del self._maybe_delete[save_path]
self._maybe_delete[save_path] = timestamp
self._latest_checkpoint = save_path
# Before deleting anything we update the Checkpoint proto with the new
# checkpoint. We'll go back and correct it after cleaning up old files,
# but a preemption while deleting will be more likely to see the new
# checkpoint this way.
self._record_state()
self._sweep()
# Write out the Checkpoint proto a second time, now without the deleted
# checkpoints.
self._record_state()
