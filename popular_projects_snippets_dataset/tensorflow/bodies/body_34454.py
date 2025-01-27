# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
with self.cached_session():
    q = data_flow_ops.FIFOQueue(10, dtypes_lib.float32)
    enqueue_op = q.enqueue((10.0,))
    close_op = q.close()

    enqueue_op.run()
    close_op.run()

    # Expect the operation to fail due to the queue being closed.
    with self.assertRaisesRegex(errors_impl.CancelledError, "is closed"):
        enqueue_op.run()
