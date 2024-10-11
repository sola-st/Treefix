# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver.py
"""Recovers the internal saver state after a crash.

    This method is useful for recovering the "self._last_checkpoints" state.

    Globs for the checkpoints pointed to by `checkpoint_paths`.  If the files
    exist, use their mtime as the checkpoint timestamp.

    Args:
      checkpoint_paths: a list of checkpoint paths.
    """
checkpoints_with_mtimes = []
for checkpoint_path in checkpoint_paths:
    try:
        mtime = checkpoint_management.get_checkpoint_mtimes([checkpoint_path])
    except errors.NotFoundError:
        # It's fine if some other thread/process is deleting some older
        # checkpoint concurrently.
        continue
    if mtime:
        checkpoints_with_mtimes.append((checkpoint_path, mtime[0]))
self.set_last_checkpoints_with_time(checkpoints_with_mtimes)
