# Extracted from ./data/repos/tensorflow/tensorflow/python/training/queue_runner_test.py
with self.cached_session() as sess:
    queue = data_flow_ops.FIFOQueue(10, dtypes.float32)
    qr = queue_runner_impl.QueueRunner(queue, [_MockOp("not an op")])
    coord = coordinator.Coordinator()
    threads = qr.create_threads(sess, coord)
    for t in threads:
        t.start()
    # The exception should be re-raised when joining.
    with self.assertRaisesRegex(ValueError, "Operation not in the graph"):
        coord.join()
