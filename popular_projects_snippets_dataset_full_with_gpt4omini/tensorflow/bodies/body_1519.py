# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/fifo_queue_test.py
with self.session() as sess, self.test_scope():
    q = data_flow_ops.FIFOQueue(10, dtypes_lib.float32)
    elems = [10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0]
    enqueue_ops = [q.enqueue((x,)) for x in elems]
    dequeued_t = q.dequeue()

    # Enqueue every element using a single thread.
    for enqueue_op in enqueue_ops:
        enqueue_op.run()

    # Run one consumer thread for each element in elems.
    results = []

    def dequeue():
        results.append(sess.run(dequeued_t))

    threads = [self.checkedThread(target=dequeue) for _ in enqueue_ops]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    self.assertItemsEqual(elems, results)
