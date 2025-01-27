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
