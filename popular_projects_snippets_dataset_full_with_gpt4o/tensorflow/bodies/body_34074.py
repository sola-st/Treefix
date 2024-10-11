# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/barrier_ops_test.py
with self.cached_session() as sess:
    b = data_flow_ops.Barrier(dtypes.float32, shapes=())
    size_t = b.ready_size()
    keys = [str(x).encode("ascii") for x in range(10)]
    values = [float(x) for x in range(10)]
    insert_ops = [b.insert_many(0, [k], [v]) for k, v in zip(keys, values)]
    take_t = b.take_many(10)

    self.evaluate(insert_ops)
    self.assertEqual(self.evaluate(size_t), [10])

    indices_val, keys_val, values_val = sess.run(
        [take_t[0], take_t[1], take_t[2][0]])

self.assertAllEqual(indices_val, [-2**63 + x for x in range(10)])
for k, v in zip(keys, values):
    idx = keys_val.tolist().index(k)
    self.assertEqual(values_val[idx], v)
