# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver.py
"""DEPRECATED: Use set_last_checkpoints_with_time.

    Sets the list of old checkpoint filenames.

    Args:
      last_checkpoints: A list of checkpoint filenames.

    Raises:
      AssertionError: If last_checkpoints is not a list.
    """
assert isinstance(last_checkpoints, list)
# We use a timestamp of +inf so that this checkpoint will never be
# deleted.  This is both safe and backwards compatible to a previous
# version of the code which used s[1] as the "timestamp".
self._last_checkpoints = [(s, np.inf) for s in last_checkpoints]
