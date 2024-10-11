# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
with self.cached_session() as sess:
    q = data_flow_ops.FIFOQueue(10, dtypes_lib.int32, shapes=())
    enqueue_placeholder = array_ops.placeholder(dtypes_lib.int32, shape=())
    enqueue_op = q.enqueue((enqueue_placeholder,))
    enqueuemany_placeholder = array_ops.placeholder(
        dtypes_lib.int32, shape=(None,))
    enqueuemany_op = q.enqueue_many((enqueuemany_placeholder,))

    dequeued_t = q.dequeue()
    close_op = q.close()

    def dequeue():
        for i in range(250):
            self.assertEqual(i, self.evaluate(dequeued_t))

    dequeue_thread = self.checkedThread(target=dequeue)
    dequeue_thread.start()

    elements_enqueued = 0
    while elements_enqueued < 250:
        # With equal probability, run Enqueue or enqueue_many.
        if random.random() > 0.5:
            enqueue_op.run({enqueue_placeholder: elements_enqueued})
            elements_enqueued += 1
        else:
            count = random.randint(0, min(20, 250 - elements_enqueued))
            range_to_enqueue = np.arange(
                elements_enqueued, elements_enqueued + count, dtype=np.int32)
            enqueuemany_op.run({enqueuemany_placeholder: range_to_enqueue})
            elements_enqueued += count

    close_op.run()
    dequeue_thread.join()
    self.assertEqual(0, q.size().eval())
