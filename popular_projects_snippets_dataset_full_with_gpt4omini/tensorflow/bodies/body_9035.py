# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
"""Raises the error if one exists.

    If an error exists, cancel the closures in queue, raises it, and clear
    the error.

    This method expects self._queue_lock to be held prior to entry.
    """
if self._error:
    logging.error("Start cancelling closures due to error %r: %s",
                  self._error, self._error)
    self._cancel_all_closures()
    try:
        raise self._error  # pylint: disable=raising-bad-type
    finally:
        self._error = None
