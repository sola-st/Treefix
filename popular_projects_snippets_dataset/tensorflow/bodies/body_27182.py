# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/multi_process_cluster.py
super(_RemoteWorkerProcess, self).__init__()
self._dispatcher_address = dispatcher_address
self._port = port
self._worker_tags = worker_tags
self._pipe_writer = pipe_writer
