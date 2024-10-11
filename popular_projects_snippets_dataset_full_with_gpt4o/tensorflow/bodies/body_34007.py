# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/padding_fifo_queue_test.py
with self.cached_session() as sess:
    q = data_flow_ops.PaddingFIFOQueue(10, dtypes_lib.int32, shapes=((),))
    enqueue_op = q.enqueue_many((np.arange(250, dtype=np.int32),))
    dequeued_t = q.dequeue()
    count_placeholder = array_ops.placeholder(dtypes_lib.int32, shape=())
    dequeuemany_t = q.dequeue_many(count_placeholder)

    def enqueue():
        self.evaluate(enqueue_op)

    enqueue_thread = self.checkedThread(target=enqueue)
    enqueue_thread.start()

    elements_dequeued = 0
    while elements_dequeued < 250:
        # With equal probability, run Dequeue or dequeue_many.
        if random.random() > 0.5:
            self.assertEqual(elements_dequeued, self.evaluate(dequeued_t))
            elements_dequeued += 1
        else:
            count = random.randint(0, min(20, 250 - elements_dequeued))
            expected_range = np.arange(
                elements_dequeued, elements_dequeued + count, dtype=np.int32)
            self.assertAllEqual(expected_range,
                                dequeuemany_t.eval({
                                    count_placeholder: count
                                }))
            elements_dequeued += count

    q.close().run()
    enqueue_thread.join()
    self.assertEqual(0, q.size().eval())
