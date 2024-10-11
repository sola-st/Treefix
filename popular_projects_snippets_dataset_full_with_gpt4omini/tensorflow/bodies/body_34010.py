# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/padding_fifo_queue_test.py
# We need each thread to keep its own device stack or the device scopes
# won't be properly nested.
ops.get_default_graph().switch_to_thread_local()
with self.cached_session() as sess:
    q = data_flow_ops.PaddingFIFOQueue(10, dtypes_lib.float32, ((),))
    elems = [10.0, 20.0, 30.0, 40.0]
    enqueue_op = q.enqueue_many((elems,))
    dequeued_t = q.dequeue_many(4)

    dequeued_elems = []

    def enqueue():
        # The enqueue_op should run after the dequeue op has blocked.
        # TODO(mrry): Figure out how to do this without sleeping.
        time.sleep(0.1)
        self.evaluate(enqueue_op)

    def dequeue():
        dequeued_elems.extend(self.evaluate(dequeued_t).tolist())

    enqueue_thread = self.checkedThread(target=enqueue)
    dequeue_thread = self.checkedThread(target=dequeue)
    enqueue_thread.start()
    dequeue_thread.start()
    enqueue_thread.join()
    dequeue_thread.join()

    self.assertAllEqual(elems, dequeued_elems)
