# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib_test.py
server = self._cached_server
with ops.Graph().as_default():
    q = data_flow_ops.FIFOQueue(1, [dtypes.float32])
    blocking_t = q.dequeue()

    with session.Session(server.target) as sess:
        with self.assertRaises(errors_impl.DeadlineExceededError):
            sess.run(
                blocking_t, options=config_pb2.RunOptions(timeout_in_ms=1000))

    with session.Session(server.target, config=self._useRPCConfig()) as sess:
        with self.assertRaises(errors_impl.DeadlineExceededError):
            sess.run(
                blocking_t, options=config_pb2.RunOptions(timeout_in_ms=1000))
