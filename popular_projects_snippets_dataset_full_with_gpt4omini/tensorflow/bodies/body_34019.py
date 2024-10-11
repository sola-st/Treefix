# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/padding_fifo_queue_test.py
with self.cached_session() as sess:
    q = data_flow_ops.PaddingFIFOQueue(10, dtypes_lib.float32, ((),))
    elems = [10.0, 20.0, 30.0, 40.0]
    enqueue_op = q.enqueue_many((elems,))
    close_op = q.close()
    dequeued_t = q.dequeue_up_to(3)

    enqueue_op.run()

    def dequeue():
        self.assertAllEqual(elems[:3], self.evaluate(dequeued_t))
        self.assertAllEqual(elems[3:], self.evaluate(dequeued_t))

    dequeue_thread = self.checkedThread(target=dequeue)
    dequeue_thread.start()
    # The close_op should run after the dequeue_thread has blocked.
    # TODO(mrry): Figure out how to do this without sleeping.
    time.sleep(0.1)
    close_op.run()
    dequeue_thread.join()
