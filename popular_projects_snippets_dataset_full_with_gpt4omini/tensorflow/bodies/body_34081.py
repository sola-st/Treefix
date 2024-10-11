# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/barrier_ops_test.py
with self.cached_session() as sess:
    b = data_flow_ops.Barrier(
        (dtypes.float32, dtypes.float32), shapes=((), ()), name="B")
    size_t = b.ready_size()
    incomplete_t = b.incomplete_size()
    keys = [b"a", b"b", b"c"]
    values_0 = [10.0, 20.0, 30.0]
    values_1 = [100.0, 200.0, 300.0]
    insert_0_op = b.insert_many(0, keys, values_0)
    insert_1_op = b.insert_many(1, keys, values_1)
    close_op = b.close()
    fail_insert_op = b.insert_many(0, ["f"], [60.0])
    take_t = b.take_many(3)
    take_too_many_t = b.take_many(4)

    self.assertEqual(self.evaluate(size_t), [0])
    self.assertEqual(self.evaluate(incomplete_t), [0])
    insert_0_op.run()
    self.assertEqual(self.evaluate(size_t), [0])
    self.assertEqual(self.evaluate(incomplete_t), [3])
    close_op.run()

    # This op should fail because the barrier is closed.
    with self.assertRaisesOpError("is closed"):
        fail_insert_op.run()

    # This op should succeed because the barrier has not canceled
    # pending enqueues
    insert_1_op.run()
    self.assertEqual(self.evaluate(size_t), [3])
    self.assertEqual(self.evaluate(incomplete_t), [0])

    # This op should fail because the barrier is closed.
    with self.assertRaisesOpError("is closed"):
        fail_insert_op.run()

    # This op should fail because we requested more elements than are
    # available in incomplete + ready queue.
    with self.assertRaisesOpError(r"is closed and has insufficient elements "
                                  r"\(requested 4, total size 3\)"):
        sess.run(take_too_many_t[0])  # Sufficient to request just the indices

    # This op should succeed because there are still completed elements
    # to process.
    indices_val, keys_val, values_0_val, values_1_val = sess.run(
        [take_t[0], take_t[1], take_t[2][0], take_t[2][1]])
    self.assertAllEqual(indices_val, [-2**63] * 3)
    for k, v0, v1 in zip(keys, values_0, values_1):
        idx = keys_val.tolist().index(k)
        self.assertEqual(values_0_val[idx], v0)
        self.assertEqual(values_1_val[idx], v1)

    # This op should fail because there are no more completed elements and
    # the queue is closed.
    with self.assertRaisesOpError("is closed and has insufficient elements"):
        sess.run(take_t[0])
