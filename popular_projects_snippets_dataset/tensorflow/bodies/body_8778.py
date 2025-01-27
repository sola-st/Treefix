# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/values.py
"""Initializes a `RemoteValueImpl`.

    Args:
      closure: The closure from which the `RemoteValue` is created.
      type_spec: The type spec for this `RemoteValue` which is used to trace
        functions that take this `RemoteValue` as input.
    """
self._closure = closure
self._type_spec = type_spec
self._values = None
self._has_fetched_to_local = False
self._has_fetched_to_local_lock = threading.Lock()
self._fetched_tensors = None
self._error = None
self._status_available_event = threading.Event()
self._status = RemoteValueStatus.NOT_READY
