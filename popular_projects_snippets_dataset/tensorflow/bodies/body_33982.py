# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/padding_fifo_queue_test.py
with self.cached_session():
    q = data_flow_ops.PaddingFIFOQueue(10, dtypes_lib.float32, ((),))
    elems = [10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0]
    enqueue_op = q.enqueue_many((elems,))
    dequeued_t = q.dequeue_up_to(4)

    enqueue_op.run()

    self.assertAllEqual(elems[0:4], self.evaluate(dequeued_t))
    self.assertAllEqual(elems[4:8], self.evaluate(dequeued_t))
