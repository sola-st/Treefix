# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/fifo_queue_test.py
with self.session() as sess, self.test_scope():
    q = data_flow_ops.FIFOQueue(3, dtypes_lib.float32)
    elems = [10.0, 20.0, 30.0]
    enqueue_ops = [q.enqueue((x,)) for x in elems]
    dequeued_t = q.dequeue()

    def enqueue():
        # The enqueue_ops should run after the dequeue op has blocked.
        # TODO(mrry): Figure out how to do this without sleeping.
        time.sleep(0.1)
        for enqueue_op in enqueue_ops:
            sess.run(enqueue_op)

    results = []

    def dequeue():
        for _ in range(len(elems)):
            results.append(sess.run(dequeued_t))

    enqueue_thread = self.checkedThread(target=enqueue)
    dequeue_thread = self.checkedThread(target=dequeue)
    enqueue_thread.start()
    dequeue_thread.start()
    enqueue_thread.join()
    dequeue_thread.join()

    for elem, result in zip(elems, results):
        self.assertEqual([elem], result)
