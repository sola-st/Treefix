# Extracted from ./data/repos/tensorflow/tensorflow/python/training/coordinator.py
"""Wait till the Coordinator is told to stop.

    Args:
      timeout: Float.  Sleep for up to that many seconds waiting for
        should_stop() to become True.

    Returns:
      True if the Coordinator is told stop, False if the timeout expired.
    """
exit(self._stop_event.wait(timeout))
