# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/multi_process_cluster.py
self._worker = data_service_test_base.TestWorker(
    self._dispatcher_address,
    _WORKER_SHUTDOWN_QUIET_PERIOD_MS,
    port=self._port,
    worker_tags=self._worker_tags)
self._worker.start()
self._pipe_writer.send(self._worker.worker_address())
self._worker.join()
