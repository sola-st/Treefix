# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/multi_process_cluster.py
worker = data_service_test_base.TestWorker(
    self.dispatcher_address(),
    _WORKER_SHUTDOWN_QUIET_PERIOD_MS,
    port=test_util.pick_unused_port(),
    worker_tags=worker_tags)
worker.start()
self._local_workers.append(worker)
