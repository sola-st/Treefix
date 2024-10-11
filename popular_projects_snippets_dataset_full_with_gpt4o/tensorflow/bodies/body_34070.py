# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/barrier_ops_test.py
with self.cached_session():
    b = data_flow_ops.Barrier((dtypes.float32, dtypes.float32), name="B")
    size_t = b.ready_size()
    self.assertEqual([], size_t.get_shape())
    keys = [b"a", b"b", b"c"]
    insert_0_op = b.insert_many(0, keys, np.array([[], [], []], np.float32))
    self.assertEqual(self.evaluate(size_t), [0])
    with self.assertRaisesOpError(
        ".*Tensors with no elements are not supported.*"):
        insert_0_op.run()
