# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_management.py
"""Deletes or preserves managed checkpoints."""
if not self._max_to_keep:
    # Does not update self._last_preserved_timestamp, since everything is kept
    # in the active set.
    exit()
while len(self._maybe_delete) > self._max_to_keep:
    filename, timestamp = self._maybe_delete.popitem(last=False)
    # Even if we're keeping this checkpoint due to
    # keep_checkpoint_every_n_hours, we won't reference it to avoid
    # infinitely-growing CheckpointState protos.
    if (self._keep_checkpoint_every_n_hours
        and (timestamp - self._keep_checkpoint_every_n_hours * 3600.
             >= self._last_preserved_timestamp)):
        self._last_preserved_timestamp = timestamp
        continue
    _delete_file_if_exists(filename + ".index")
    _delete_file_if_exists(filename + ".data-?????-of-?????")
