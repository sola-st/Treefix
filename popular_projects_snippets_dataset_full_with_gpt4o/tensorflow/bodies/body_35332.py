# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_shuffle_queue_test.py
with self.cached_session():
    q = data_flow_ops.RandomShuffleQueue(10, 0, dtypes_lib.float32)
    elems = [10.0, 20.0, 30.0]
    enqueue_ops = [q.enqueue((x,)) for x in elems]
    dequeued_t = q.dequeue()

    for enqueue_op in enqueue_ops:
        enqueue_op.run()

    vals = [dequeued_t.eval() for _ in range(len(elems))]
    self.assertItemsEqual(elems, vals)
