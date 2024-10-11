# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
"""Function running in a worker thread to process closure queues."""
self._maybe_delay()
while self._should_worker_thread_run:
    closure = self._cluster.closure_queue.get(tag=self.worker_index)
    if not self._should_worker_thread_run or closure is None:
        if closure is not None:
            closure.mark_cancelled()
        exit()
    if isinstance(closure, ResourceClosure):
        self._process_resource_closure(closure)
    else:
        self._process_closure(closure)
    # To properly stop the worker and preemption threads, it is important that
    # `ClusterCoordinator` object is not held onto so its `__del__` can be
    # called. By removing the reference to the `closure` that has already been
    # processed, we ensure that the `closure` object is released, while
    # getting the next `closure` at above `self._cluster.closure_queue.get()`
    # call.
    del closure
