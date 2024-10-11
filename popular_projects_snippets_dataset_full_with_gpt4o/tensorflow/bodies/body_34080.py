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
        b.insert_many(0, keys_i(i), values_0 + i)
        for i in range(num_iterations)
    ]
    insert_1_ops = [
        b.insert_many(1, keys_i(i), values_1 + i)
        for i in range(num_iterations)
    ]
    take_ops = [b.take_many(10) for _ in range(num_iterations)]

    def take(sess, i, taken):
        indices_val, keys_val, values_0_val, values_1_val = sess.run([
            take_ops[i][0], take_ops[i][1], take_ops[i][2][0], take_ops[i][2][1]
        ])
        taken.append({
            "indices": indices_val,
            "keys": keys_val,
            "values_0": values_0_val,
            "values_1": values_1_val
        })

    def insert(sess, i):
        sess.run([insert_0_ops[i], insert_1_ops[i]])

    taken = []

    take_threads = [
        self.checkedThread(
            target=take, args=(sess, i, taken)) for i in range(num_iterations)
    ]
    insert_threads = [
        self.checkedThread(
            target=insert, args=(sess, i)) for i in range(num_iterations)
    ]

    for t in take_threads:
        t.start()
    time.sleep(0.1)
    for t in insert_threads:
        t.start()
    for t in take_threads:
        t.join()
    for t in insert_threads:
        t.join()

    self.assertEqual(len(taken), num_iterations)
    flatten = lambda l: [item for sublist in l for item in sublist]
    all_indices = sorted(flatten([t_i["indices"] for t_i in taken]))
    all_keys = sorted(flatten([t_i["keys"] for t_i in taken]))

    expected_keys = sorted(
        flatten([keys_i(i) for i in range(num_iterations)]))
    expected_indices = sorted(
        flatten([-2**63 + j] * 10 for j in range(num_iterations)))

    self.assertAllEqual(all_indices, expected_indices)
    self.assertAllEqual(all_keys, expected_keys)

    for taken_i in taken:
        outer_indices_from_keys = np.array(
            [int(k.decode("ascii").split(":")[0]) for k in taken_i["keys"]])
        inner_indices_from_keys = np.array(
            [int(k.decode("ascii").split(":")[1]) for k in taken_i["keys"]])
        self.assertAllEqual(taken_i["values_0"],
                            outer_indices_from_keys + inner_indices_from_keys)
        expected_values_1 = np.vstack(
            (1 + outer_indices_from_keys + inner_indices_from_keys,
             2 + outer_indices_from_keys + inner_indices_from_keys)).T
        self.assertAllEqual(taken_i["values_1"], expected_values_1)
