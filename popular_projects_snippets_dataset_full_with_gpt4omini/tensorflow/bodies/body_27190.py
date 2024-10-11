# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/multi_process_cluster.py
"""Runs a tf.data service worker in a remote process."""

pipe_reader, pipe_writer = multi_process_lib.multiprocessing.Pipe(
    duplex=False)
worker_process = _RemoteWorkerProcess(
    self.dispatcher_address(),
    port=test_util.pick_unused_port(),
    worker_tags=worker_tags,
    pipe_writer=pipe_writer)
worker_process.start()
worker_address = pipe_reader.recv()
self._remote_workers.append((worker_address, worker_process))
