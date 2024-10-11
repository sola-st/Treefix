# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver.py
"""Sets the list of old checkpoint filenames and timestamps.

    Args:
      last_checkpoints_with_time: A list of tuples of checkpoint filenames and
        timestamps.

    Raises:
      AssertionError: If last_checkpoints_with_time is not a list.
    """
assert isinstance(last_checkpoints_with_time, list)
self._last_checkpoints = last_checkpoints_with_time
