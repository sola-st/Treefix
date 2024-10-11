# Extracted from ./data/repos/tensorflow/tensorflow/python/training/queue_runner_test.py
with self.cached_session() as sess:
    q0 = data_flow_ops.FIFOQueue(3, dtypes.float32)
    enqueue0 = q0.enqueue((10.0,))
    close0 = q0.close()
    q1 = data_flow_ops.FIFOQueue(30, dtypes.float32)
    enqueue1 = q1.enqueue((q0.dequeue(),))
    dequeue1 = q1.dequeue()
    qr = queue_runner_impl.QueueRunner(q1, [enqueue1])
    threads = qr.create_threads(sess)
    for t in threads:
        t.start()
    # Enqueue 2 values, then close queue0.
    enqueue0.run()
    enqueue0.run()
    close0.run()
    # Wait for the queue runner to terminate.
    for t in threads:
        t.join()
    # It should have terminated cleanly.
    self.assertEqual(0, len(qr.exceptions_raised))
    # The 2 values should be in queue1.
    self.assertEqual(10.0, self.evaluate(dequeue1))
    self.assertEqual(10.0, self.evaluate(dequeue1))
    # And queue1 should now be closed.
    with self.assertRaisesRegex(errors_impl.OutOfRangeError, "is closed"):
        self.evaluate(dequeue1)
