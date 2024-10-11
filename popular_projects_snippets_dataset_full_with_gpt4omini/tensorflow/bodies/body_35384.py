# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_shuffle_queue_test.py
with self.cached_session():
    q = data_flow_ops.RandomShuffleQueue(10, 4, dtypes_lib.float32)
    enqueue_op = q.enqueue((10.0,))
    close_op = q.close()

    enqueue_op.run()
    close_op.run()

    # Expect the operation to fail due to the queue being closed.
    with self.assertRaisesRegex(errors_impl.CancelledError, "is closed"):
        enqueue_op.run()
