from threading import Lock, Condition # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
self._queue_lock = Lock() # pragma: no cover
self._should_process_closures = False # pragma: no cover
self._cancellation_mgr = type('MockCancellationManager', (object,), {'start_cancel': lambda self: None})() # pragma: no cover
self._closures_queued_condition = Condition(self._queue_lock) # pragma: no cover
self._watchdog = type('MockWatchdog', (object,), {'stop': lambda self: None})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
from l3.Runtime import _l_
with self._queue_lock:
    _l_(17138)

    self._should_process_closures = False
    _l_(17135)
    self._cancellation_mgr.start_cancel()
    _l_(17136)
    self._closures_queued_condition.notify_all()
    _l_(17137)
self._watchdog.stop()
_l_(17139)
