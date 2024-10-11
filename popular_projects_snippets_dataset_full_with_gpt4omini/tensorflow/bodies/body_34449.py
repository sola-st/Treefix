# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
with self.cached_session() as sess:
    q = data_flow_ops.FIFOQueue(4, (dtypes_lib.float32, dtypes_lib.float32), (
        (), ()))
    elems_a = [1.0, 2.0, 3.0]
    elems_b = [10.0, 20.0, 30.0]
    enqueue_op = q.enqueue_many((elems_a, elems_b))
    dequeued_a_t, dequeued_b_t = q.dequeue_many(4)
    cleanup_dequeue_a_t, cleanup_dequeue_b_t = q.dequeue()
    close_op = q.close()

    enqueue_op.run()

    def dequeue():
        with self.assertRaises(errors_impl.OutOfRangeError):
            self.evaluate([dequeued_a_t, dequeued_b_t])

    dequeue_thread = self.checkedThread(target=dequeue)
    dequeue_thread.start()
    # The close_op should run after the dequeue_thread has blocked.
    # TODO(mrry): Figure out how to do this without sleeping.
    time.sleep(0.1)

    close_op.run()
    dequeue_thread.join()
    # Test that the elements in the partially-dequeued batch are
    # restored in the correct order.
    for elem_a, elem_b in zip(elems_a, elems_b):
        val_a, val_b = self.evaluate([cleanup_dequeue_a_t, cleanup_dequeue_b_t])
        self.assertEqual(elem_a, val_a)
        self.assertEqual(elem_b, val_b)
    self.assertEqual(0, q.size().eval())
