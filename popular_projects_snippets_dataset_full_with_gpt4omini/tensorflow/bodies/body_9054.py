# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
"""Clear tagged queue to ensure resource closures are rebuilt.

    Args:
      e: The exception arisen from the resource closure.
    """
logging.info("[Worker %d] Clearing tagged queue after resource closure "
             "failure.", self.worker_index)
with self._resource_tracking_lock:
    self._is_dead_with_error = e
    # No locking on queue is needed since
    #  * get will not happen concurrently here.
    #  * put to the specific tagged queue will be guarded by
    #    `self._resource_tracking_lock`.
    self._cluster.closure_queue.clear_tag_unlocked(self.worker_index)
    self._set_resources_aborted(e)
