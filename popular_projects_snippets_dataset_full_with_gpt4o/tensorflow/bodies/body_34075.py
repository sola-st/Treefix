# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/barrier_ops_test.py
with self.cached_session() as sess:
    b = data_flow_ops.Barrier(dtypes.float32, shapes=())
    size_t = b.ready_size()
    keys = [str(x).encode("ascii") for x in range(10)]
    values = [float(x) for x in range(10)]
    insert_op = b.insert_many(0, keys, values)
    take_t = [b.take_many(1) for _ in keys]

    insert_op.run()
    self.assertEqual(self.evaluate(size_t), [10])

    index_fetches = []
    key_fetches = []
    value_fetches = []
    for ix_t, k_t, v_t in take_t:
        index_fetches.append(ix_t)
        key_fetches.append(k_t)
        value_fetches.append(v_t[0])
    vals = sess.run(index_fetches + key_fetches + value_fetches)

index_vals = vals[:len(keys)]
key_vals = vals[len(keys):2 * len(keys)]
value_vals = vals[2 * len(keys):]

taken_elems = []
for k, v in zip(key_vals, value_vals):
    taken_elems.append((k[0], v[0]))

self.assertAllEqual(np.hstack(index_vals), [-2**63] * 10)

self.assertItemsEqual(
    zip(keys, values), [(k[0], v[0]) for k, v in zip(key_vals, value_vals)])
