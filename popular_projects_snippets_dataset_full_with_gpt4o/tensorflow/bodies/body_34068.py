# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/barrier_ops_test.py
with self.cached_session():
    b = data_flow_ops.Barrier(
        (dtypes.float32, dtypes.float32), shapes=((), ()), name="B")
    size_t = b.ready_size()
    self.assertEqual([], size_t.get_shape())
    keys = [b"a", b"b", b"c"]
    insert_0_op = b.insert_many(0, keys, [10.0, 20.0, 30.0])
    insert_1_op = b.insert_many(1, keys, [100.0, 200.0, 300.0])

    self.assertEqual(self.evaluate(size_t), [0])
    insert_0_op.run()
    self.assertEqual(self.evaluate(size_t), [0])
    insert_1_op.run()
    self.assertEqual(self.evaluate(size_t), [3])
