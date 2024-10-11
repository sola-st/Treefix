# Extracted from ./data/repos/tensorflow/tensorflow/python/training/queue_runner_test.py
with self.cached_session() as sess:
    # The enqueue will quickly block.
    queue = data_flow_ops.FIFOQueue(2, dtypes.float32)
    enqueue = queue.enqueue((10.0,))
    dequeue = queue.dequeue()
    qr = queue_runner_impl.QueueRunner(queue, [enqueue])
    coord = coordinator.Coordinator()
    qr.create_threads(sess, coord, start=True)
    # Dequeue one element and then request stop.
    dequeue.op.run()
    time.sleep(0.02)
    coord.request_stop()
    # We should be able to join because the RequestStop() will cause
    # the queue to be closed and the enqueue to terminate.
    coord.join(stop_grace_period_secs=1.0)
