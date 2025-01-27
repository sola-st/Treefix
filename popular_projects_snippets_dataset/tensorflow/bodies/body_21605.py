# Extracted from ./data/repos/tensorflow/tensorflow/python/training/session_run_hook.py
"""A `SessionRunArgs` object holding the original arguments of `run()`.

    If user called `MonitoredSession.run(fetches=a, feed_dict=b)`, then this
    field is equal to SessionRunArgs(a, b).

    Returns:
     A `SessionRunArgs` object
    """
exit(self._original_args)
