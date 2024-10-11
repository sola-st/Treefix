# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
with self.cached_session():
    # Define a first queue that contains integer counts.
    dequeue_counts = [random.randint(1, 10) for _ in range(100)]
    count_q = data_flow_ops.FIFOQueue(100, dtypes_lib.int32, ())
    enqueue_counts_op = count_q.enqueue_many((dequeue_counts,))
    total_count = sum(dequeue_counts)

    # Define a second queue that contains total_count elements.
    elems = [random.randint(0, 100) for _ in range(total_count)]
    q = data_flow_ops.FIFOQueue(total_count, dtypes_lib.int32, ())
    enqueue_elems_op = q.enqueue_many((elems,))

    # Define a subgraph that first dequeues a count, then DequeuesMany
    # that number of elements.
    dequeued_t = q.dequeue_many(count_q.dequeue())

    enqueue_counts_op.run()
    enqueue_elems_op.run()

    dequeued_elems = []
    for _ in dequeue_counts:
        dequeued_elems.extend(self.evaluate(dequeued_t))
    self.assertEqual(elems, dequeued_elems)
