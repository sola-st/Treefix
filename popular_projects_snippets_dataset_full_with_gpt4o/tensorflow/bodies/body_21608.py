# Extracted from ./data/repos/tensorflow/tensorflow/python/training/session_run_hook.py
"""Sets stop requested field.

    Hooks can use this function to request stop of iterations.
    `MonitoredSession` checks whether this is called or not.
    """
self._stop_requested = True
