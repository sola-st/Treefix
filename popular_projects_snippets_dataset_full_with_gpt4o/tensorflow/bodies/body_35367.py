# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_shuffle_queue_test.py
with self.cached_session():
    q = data_flow_ops.RandomShuffleQueue(10, 2, dtypes_lib.float32)
    elems = [10.0, 20.0, 30.0, 40.0]
    enqueue_op = q.enqueue_many((elems,))
    close_op = q.close()
    dequeued_t = q.dequeue()

    enqueue_op.run()
    close_op.run()
    results = [dequeued_t.eval() for _ in elems]
    expected = [[elem] for elem in elems]
    self.assertItemsEqual(expected, results)

    # Expect the operation to fail due to the queue being closed.
    with self.assertRaisesRegex(errors_impl.OutOfRangeError,
                                "is closed and has insufficient"):
        self.evaluate(dequeued_t)
