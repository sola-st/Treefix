class MockCancellationManager:# pragma: no cover
    def start_cancel(self): pass # pragma: no cover
class MockWatchdog:# pragma: no cover
    def stop(self): pass # pragma: no cover

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
