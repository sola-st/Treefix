# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
with self.session(
    config=config_pb2.ConfigProto(operation_timeout_in_ms=20)) as sess:
    q = data_flow_ops.FIFOQueue(10, dtypes_lib.float32)
    self.assertEqual(
        compat.as_bytes(""), q.queue_ref.op.get_attr("container"))
    dequeued_t = q.dequeue()

    # Intentionally do not run any enqueue_ops so that dequeue will block
    # until operation_timeout_in_ms.
    with self.assertRaisesRegex(errors_impl.DeadlineExceededError,
                                "Timed out waiting for notification"):
        self.evaluate(dequeued_t)
