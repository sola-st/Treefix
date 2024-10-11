# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/barrier_ops_test.py
with self.cached_session() as sess:
    b = data_flow_ops.Barrier(dtypes.float32, shapes=())
    keys = [str(x).encode("ascii") for x in range(10)]
    values = [float(x) for x in range(10)]
    insert_ops = [b.insert_many(0, [k], [v]) for k, v in zip(keys, values)]
    take_t = b.take_many(10)

    def take():
        indices_val, keys_val, values_val = sess.run(
            [take_t[0], take_t[1], take_t[2][0]])
        self.assertAllEqual(indices_val,
                            [int(x.decode("ascii")) - 2**63 for x in keys_val])
        self.assertItemsEqual(zip(keys, values), zip(keys_val, values_val))

    t = self.checkedThread(target=take)
    t.start()
    time.sleep(0.1)
    for insert_op in insert_ops:
        insert_op.run()
    t.join()
