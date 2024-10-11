# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/values.py
self._status = RemoteValueStatus.READY
self._values = None
self._error = error
self._status_available_event.set()
