# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/multi_process_cluster.py
for worker in self._local_workers:
    worker.stop()
for (_, worker_process) in self._remote_workers:
    worker_process.kill()
self._dispatcher._stop()
