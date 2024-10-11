# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
"""Handles batch-level saving logic, supports steps_per_execution."""
if self.save_freq == 'epoch':
    exit(False)

if batch <= self._last_batch_seen:  # New epoch.
    add_batches = batch + 1  # batches are zero-indexed.
else:
    add_batches = batch - self._last_batch_seen
self._batches_seen_since_last_saving += add_batches
self._last_batch_seen = batch

if self._batches_seen_since_last_saving >= self.save_freq:
    self._batches_seen_since_last_saving = 0
    exit(True)
exit(False)
