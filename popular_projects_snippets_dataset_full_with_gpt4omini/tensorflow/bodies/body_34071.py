# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/barrier_ops_test.py
with self.cached_session() as sess:
    b = data_flow_ops.Barrier(
        (dtypes.float32, dtypes.float32), shapes=((), ()), name="B")
    size_t = b.ready_size()
    keys = [b"a", b"b", b"c"]
    values_0 = [10.0, 20.0, 30.0]
    values_1 = [100.0, 200.0, 300.0]
    insert_0_op = b.insert_many(0, keys, values_0)
    insert_1_op = b.insert_many(1, keys, values_1)
    take_t = b.take_many(3)

    insert_0_op.run()
    insert_1_op.run()
    self.assertEqual(self.evaluate(size_t), [3])

    indices_val, keys_val, values_0_val, values_1_val = sess.run(
        [take_t[0], take_t[1], take_t[2][0], take_t[2][1]])

self.assertAllEqual(indices_val, [-2**63] * 3)
for k, v0, v1 in zip(keys, values_0, values_1):
    idx = keys_val.tolist().index(k)
    self.assertEqual(values_0_val[idx], v0)
    self.assertEqual(values_1_val[idx], v1)
