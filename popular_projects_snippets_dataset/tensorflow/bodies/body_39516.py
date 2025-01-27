# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
"""For consistency with `CheckpointLoadStatus`.

    Use `initialize_or_restore` for initializing if no checkpoint was passed
    to `Saver.restore` and restoring otherwise.

    Args:
      session: Not used.
    """
raise AssertionError(
    "No checkpoint specified, so no restore ops are available "
    "(save_path=None to Saver.restore).")
