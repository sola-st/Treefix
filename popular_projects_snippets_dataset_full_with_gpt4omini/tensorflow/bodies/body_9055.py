# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
logging.info("[Worker %d] calling _on_worker_recovery", self.worker_index)
with self._resource_tracking_lock:
    for weakref_resource in self._resource_remote_value_refs:
        resource = weakref_resource()
        if resource:
            self._schedule_resource(resource._closure)  # pylint: disable=protected-access
    self._is_dead_with_error = False
