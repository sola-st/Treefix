# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
logging.info("[Worker %d] Putting back a closure after it failed.",
             self.worker_index)
self._cluster.closure_queue.put_back(closure)

with self._resource_tracking_lock:
    self._is_dead_with_error = e
    self._set_resources_aborted(e)
