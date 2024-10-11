# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/test_base.py
worker = TestWorker(self.dispatcher_address(),
                    self._worker_shutdown_quiet_period_ms,
                    self._data_transfer_protocol)
if start:
    worker.start()
self.workers.append(worker)
