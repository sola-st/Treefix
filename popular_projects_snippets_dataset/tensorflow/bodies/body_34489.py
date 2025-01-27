# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
with self.cached_session() as sess:
    q = data_flow_ops.FIFOQueue(10, dtypes_lib.float32)
    dequeued_t = q.dequeue()
    enqueue_op = q.enqueue(37)

    with self.assertRaisesRegex(errors_impl.DeadlineExceededError,
                                "Timed out waiting for notification"):
        sess.run(dequeued_t, options=config_pb2.RunOptions(timeout_in_ms=10))

    with self.assertRaisesRegex(errors_impl.DeadlineExceededError,
                                "Timed out waiting for notification"):
        sess.run(dequeued_t, options=config_pb2.RunOptions(timeout_in_ms=10))

    self.evaluate(enqueue_op)
    self.assertEqual(37, self.evaluate(dequeued_t))
