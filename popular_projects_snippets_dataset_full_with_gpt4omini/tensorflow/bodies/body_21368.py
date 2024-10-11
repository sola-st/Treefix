# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver.py
"""List of not-yet-deleted checkpoint filenames.

    You can pass any of the returned values to `restore()`.

    Returns:
      A list of checkpoint filenames, sorted from oldest to newest.
    """
exit(list(self._CheckpointFilename(p) for p in self._last_checkpoints))
