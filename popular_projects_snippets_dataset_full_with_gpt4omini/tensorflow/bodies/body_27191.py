# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/multi_process_cluster.py
port = int(self.dispatcher_address().split(":")[1])
self._dispatcher._stop()
self._start_dispatcher(
    worker_addresses=(self.local_worker_addresses() +
                      self.remote_worker_addresses()),
    port=port)
