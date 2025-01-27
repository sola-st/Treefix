# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/barrier_ops_test.py
with self.cached_session() as sess:
    b = data_flow_ops.Barrier(
        (dtypes.float32, dtypes.int64), shapes=((), (2,)))
    num_iterations = 100
    keys = [str(x) for x in range(10)]
    values_0 = np.asarray(range(10), dtype=np.float32)
    values_1 = np.asarray([[x + 1, x + 2] for x in range(10)], dtype=np.int64)
    keys_i = lambda i: [("%d:%s" % (i, k)).encode("ascii") for k in keys]
    insert_0_ops = [
        b.insert_many(
            0, keys_i(i), values_0 + i, name="insert_0_%d" % i)
        for i in range(num_iterations)
    ]

    close_op = b.close(cancel_pending_enqueues=cancel)

    take_ops = [
        b.take_many(
            10, name="take_%d" % i) for i in range(num_iterations)
    ]
    # insert_1_ops will only run after closure
    insert_1_ops = [
        b.insert_many(
            1, keys_i(i), values_1 + i, name="insert_1_%d" % i)
        for i in range(num_iterations)
    ]

    def take(sess, i, taken):
        if cancel:
            try:
                indices_val, unused_keys_val, unused_val_0, unused_val_1 = sess.run(
                    [
                        take_ops[i][0], take_ops[i][1], take_ops[i][2][0],
                        take_ops[i][2][1]
                    ])
                taken.append(len(indices_val))
            except errors_impl.OutOfRangeError:
                taken.append(0)
        else:
            indices_val, unused_keys_val, unused_val_0, unused_val_1 = sess.run([
                take_ops[i][0], take_ops[i][1], take_ops[i][2][0],
                take_ops[i][2][1]
            ])
            taken.append(len(indices_val))

    def insert_0(sess, i):
        insert_0_ops[i].run(session=sess)

    def insert_1(sess, i):
        if cancel:
            try:
                insert_1_ops[i].run(session=sess)
            except errors_impl.CancelledError:
                pass
        else:
            insert_1_ops[i].run(session=sess)

    taken = []

    take_threads = [
        self.checkedThread(
            target=take, args=(sess, i, taken)) for i in range(num_iterations)
    ]
    insert_0_threads = [
        self.checkedThread(
            target=insert_0, args=(sess, i)) for i in range(num_iterations)
    ]
    insert_1_threads = [
        self.checkedThread(
            target=insert_1, args=(sess, i)) for i in range(num_iterations)
    ]

    for t in insert_0_threads:
        t.start()
    for t in insert_0_threads:
        t.join()
    for t in take_threads:
        t.start()

    close_op.run()

    for t in insert_1_threads:
        t.start()
    for t in take_threads:
        t.join()
    for t in insert_1_threads:
        t.join()

    if cancel:
        self.assertEqual(taken, [0] * num_iterations)
    else:
        self.assertEqual(taken, [10] * num_iterations)
