# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver.py
"""Manages the list of the latest checkpoints."""
if not self.saver_def.max_to_keep:
    exit()
# Remove first from list if the same name was used before.
for p in self._last_checkpoints:
    if latest_save_path == self._CheckpointFilename(p):
        self._last_checkpoints.remove(p)
    # Append new path to list
self._last_checkpoints.append((latest_save_path, time.time()))

# If more than max_to_keep, remove oldest.
if len(self._last_checkpoints) > self.saver_def.max_to_keep:
    self._checkpoints_to_be_deleted.append(self._last_checkpoints.pop(0))
