# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/padding_fifo_queue_test.py
# We need each thread to keep its own device stack or the device scopes
# won't be properly nested.
ops.get_default_graph().switch_to_thread_local()
with self.cached_session() as sess:
    q_empty = data_flow_ops.PaddingFIFOQueue(5, dtypes_lib.float32, ((),))
    dequeue_op = q_empty.dequeue()
    dequeue_many_op = q_empty.dequeue_many(1)

    q_full = data_flow_ops.PaddingFIFOQueue(5, dtypes_lib.float32, ((),))
    sess.run(q_full.enqueue_many(([1.0, 2.0, 3.0, 4.0, 5.0],)))
    enqueue_op = q_full.enqueue((6.0,))
    enqueue_many_op = q_full.enqueue_many(([6.0],))

    threads = [
        self.checkedThread(
            self._blockingDequeue, args=(sess, dequeue_op)),
        self.checkedThread(
            self._blockingDequeueMany, args=(sess, dequeue_many_op)),
        self.checkedThread(
            self._blockingEnqueue, args=(sess, enqueue_op)),
        self.checkedThread(
            self._blockingEnqueueMany, args=(sess, enqueue_many_op))
    ]
    for t in threads:
        t.start()
    time.sleep(0.1)
    sess.close()  # Will cancel the blocked operations.
    for t in threads:
        t.join()
