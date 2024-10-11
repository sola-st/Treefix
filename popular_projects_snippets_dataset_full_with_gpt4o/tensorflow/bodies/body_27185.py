# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/multi_process_cluster.py
self._work_dir = tempfile.mkdtemp(dir=googletest.GetTempDir())
self._deployment_mode = deployment_mode
self._start_dispatcher(worker_addresses)
self._start_local_workers(num_local_workers, worker_tags)
self._start_remote_workers(num_remote_workers, worker_tags)
