# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/values.py
self._status = RemoteValueStatus.ABORTED
self._values = None
self._error = error

# Wake up any waiting thread and clear the event.
self._status_available_event.set()
