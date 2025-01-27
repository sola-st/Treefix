# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/values.py
self._status_available_event.clear()
# TODO(yuefengz): we may need to rebuild its inputs as well.
self._closure.execute_on(worker)
