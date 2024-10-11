# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_management.py
"""Saves the `CheckpointManager`'s state in `directory`."""
filenames, timestamps = zip(*self._maybe_delete.items())
update_checkpoint_state_internal(
    self._directory,
    model_checkpoint_path=self.latest_checkpoint,
    all_model_checkpoint_paths=filenames,
    all_model_checkpoint_timestamps=timestamps,
    last_preserved_timestamp=self._last_preserved_timestamp,
    save_relative_paths=True)
