# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_shuffle_queue_test.py
with self.cached_session():
    q = data_flow_ops.RandomShuffleQueue(10, 0, dtypes_lib.float32)
    enqueue_op = q.enqueue((constant_op.constant(
        [10.0, 20.0], shape=(1, 2)),))
    dequeued_t = q.dequeue_many(0)

    # Expect the operation to fail due to the shape not being constrained.
    with self.assertRaisesOpError(
        "require the components to have specified shapes"):
        self.evaluate(dequeued_t)

    enqueue_op.run()

    # RandomShuffleQueue does not make any attempt to support DequeueMany
    # with unspecified shapes, even if a shape could be inferred from the
    # elements enqueued.
    with self.assertRaisesOpError(
        "require the components to have specified shapes"):
        self.evaluate(dequeued_t)
