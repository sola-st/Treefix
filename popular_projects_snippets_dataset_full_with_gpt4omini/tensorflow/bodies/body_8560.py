# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_test_base.py
with skip_if_grpc_server_cant_be_started(self):
    self._coord.join(worker_threads)
