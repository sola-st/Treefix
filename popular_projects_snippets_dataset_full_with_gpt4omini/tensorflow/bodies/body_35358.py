# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_shuffle_queue_test.py
with self.cached_session() as sess:
    dequeue_sizes = [random.randint(50, 150) for _ in range(10)]
    total_elements = sum(dequeue_sizes)
    q = data_flow_ops.RandomShuffleQueue(
        total_elements, 0, dtypes_lib.float32, shapes=())

    elems = [10.0 * x for x in range(total_elements)]
    enqueue_op = q.enqueue_many((elems,))
    dequeue_ops = [q.dequeue_up_to(size) for size in dequeue_sizes]

    enqueue_op.run()

    # Dequeue random number of items in parallel on 10 threads.
    dequeued_elems = []

    def dequeue(dequeue_op):
        dequeued_elems.extend(self.evaluate(dequeue_op))

    threads = []
    for dequeue_op in dequeue_ops:
        threads.append(self.checkedThread(target=dequeue, args=(dequeue_op,)))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    self.assertItemsEqual(elems, dequeued_elems)
