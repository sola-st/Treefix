# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/barrier_ops_test.py
with self.cached_session() as sess:
    b = data_flow_ops.Barrier(
        (dtypes.float32, dtypes.int64), shapes=((), (2,)))
    num_iterations = 50
    keys = [str(x) for x in range(10)]
    values_0 = np.asarray(range(10), dtype=np.float32)
    values_1 = np.asarray([[x + 1, x + 2] for x in range(10)], dtype=np.int64)
    keys_i = lambda i: [("%d:%s" % (i, k)).encode("ascii") for k in keys]
    insert_0_ops = [
        b.insert_many(0, keys_i(i), values_0 + i)
        for i in range(num_iterations)
    ]
    insert_1_ops = [
        b.insert_many(1, keys_i(i), values_1 + i)
        for i in range(num_iterations)
    ]
    take_ops = [b.take_many(10) for _ in range(num_iterations)]
    close_op = b.close(cancel_pending_enqueues=cancel)

    def take(sess, i, taken):
        try:
            indices_val, unused_keys_val, unused_val_0, unused_val_1 = sess.run([
                take_ops[i][0], take_ops[i][1], take_ops[i][2][0],
                take_ops[i][2][1]
            ])
            taken.append(len(indices_val))
        except errors_impl.OutOfRangeError:
            taken.append(0)

    def insert(sess, i):
        try:
            sess.run([insert_0_ops[i], insert_1_ops[i]])
        except errors_impl.CancelledError:
            pass

    taken = []

    take_threads = [
        self.checkedThread(
            target=take, args=(sess, i, taken)) for i in range(num_iterations)
    ]
    insert_threads = [
        self.checkedThread(
            target=insert, args=(sess, i)) for i in range(num_iterations)
    ]

    first_half_insert_threads = insert_threads[:num_iterations // 2]
    second_half_insert_threads = insert_threads[num_iterations // 2:]

    for t in take_threads:
        t.start()
    for t in first_half_insert_threads:
        t.start()
    for t in first_half_insert_threads:
        t.join()

    close_op.run()

    for t in second_half_insert_threads:
        t.start()
    for t in take_threads:
        t.join()
    for t in second_half_insert_threads:
        t.join()

    self.assertEqual(
        sorted(taken),
        [0] * (num_iterations // 2) + [10] * (num_iterations // 2))
