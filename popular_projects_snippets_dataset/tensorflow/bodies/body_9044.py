# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
self._server_def = server_def
self._cluster = cluster
self._cluster_update_lock = threading.Lock()
self._cluster_due_for_update_or_finish = threading.Event()
self._worker_up_cond = threading.Condition(self._cluster_update_lock)
self._error_from_recovery = None
self._should_preemption_thread_run = True
self._preemption_handler_thread = threading.Thread(
    target=self._preemption_handler,
    name="WorkerPreemptionHandler",
    daemon=True)
self._preemption_handler_thread.start()
