# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_shuffle_queue_test.py
with self.cached_session():
    q = data_flow_ops.RandomShuffleQueue(10, 0, dtypes_lib.float32)
    elems = [10.0, 20.0, 30.0, 40.0]
    enqueue_op = q.enqueue_many((elems,))
    dequeued_t = q.dequeue()
    enqueue_op.run()
    enqueue_op.run()

    results = []
    for _ in range(8):
        results.append(dequeued_t.eval())
    self.assertItemsEqual(elems + elems, results)
