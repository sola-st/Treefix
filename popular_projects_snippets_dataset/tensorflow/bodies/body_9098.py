# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator_test.py
self._result_correct = 0
self._lock = threading.Lock()
self._worker_context = {}
self._strategy_property = {}
self._std_servers = {}
self._barrier = distribute_coordinator._Barrier(NUM_WORKERS)
self._coord = coordinator.Coordinator()
