# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/values.py
self._status_available_event.wait()
if self._status is RemoteValueStatus.ABORTED:
    raise errors.CancelledError(
        None, None,
        "The corresponding function is aborted. Please reschedule the "
        "function.")
if self._error is not None:
    raise self._error
