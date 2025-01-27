# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/multi_process_cluster.py
self._local_workers = []
for _ in range(num_workers):
    self.start_local_worker(worker_tags)
