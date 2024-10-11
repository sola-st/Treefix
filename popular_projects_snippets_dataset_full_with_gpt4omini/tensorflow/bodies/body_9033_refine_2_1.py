self = type('Mock', (), {})() # pragma: no cover
self._should_process_closures = True # pragma: no cover
self._cancellation_mgr = type('MockCancellationMgr', (), {'start_cancel': lambda self: None})() # pragma: no cover
self._watchdog = type('MockWatchdog', (), {'stop': lambda self: None})() # pragma: no cover

class MockCancellationManager:# pragma: no cover
    def start_cancel(self): print('Cancellation started') # pragma: no cover
class MockWatchdog:# pragma: no cover
    def stop(self): print('Watchdog stopped') # pragma: no cover
self = type('Mock', (object,), {})() # pragma: no cover
self._should_process_closures = False # pragma: no cover
self._cancellation_mgr = MockCancellationManager() # pragma: no cover
self._watchdog = MockWatchdog() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
from l3.Runtime import _l_
with self._queue_lock:
    _l_(5360)

    self._should_process_closures = False
    _l_(5357)
    self._cancellation_mgr.start_cancel()
    _l_(5358)
    self._closures_queued_condition.notify_all()
    _l_(5359)
self._watchdog.stop()
_l_(5361)
