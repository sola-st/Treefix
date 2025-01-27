# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
self.worker_index = worker_index
self.device_name = device_name
self.executor = executor.new_executor(enable_async=False)
self.failure_handler = cluster.failure_handler
self._cluster = cluster
self._resource_tracking_lock = threading.Lock()
self._resource_remote_value_refs = []
self._is_dead_with_error = None
self._should_worker_thread_run = True

# Worker threads need to start after `Worker`'s initialization.
threading.Thread(target=self._process_queue,
                 name="WorkerClosureProcessingLoop-%d" % self.worker_index,
                 daemon=True).start()
