# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
self._cluster.closure_queue.put(closure, tag=self.worker_index)
