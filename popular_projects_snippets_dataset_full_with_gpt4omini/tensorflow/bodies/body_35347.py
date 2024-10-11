# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_shuffle_queue_test.py
with self.cached_session():
    q = data_flow_ops.RandomShuffleQueue(10, 0, dtypes_lib.float32, ((),))
    elems = [10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0]
    enqueue_op = q.enqueue_many((elems,))
    dequeued_t = q.dequeue_up_to(5)

    enqueue_op.run()

    results = self.evaluate(dequeued_t).tolist()
    results.extend(dequeued_t.eval())
    self.assertItemsEqual(elems, results)
