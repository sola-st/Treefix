# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/multi_process_cluster.py
# List of (worker address, remote worker process) tuples.
self._remote_workers = []
for _ in range(num_workers):
    self.start_remote_worker(worker_tags)
