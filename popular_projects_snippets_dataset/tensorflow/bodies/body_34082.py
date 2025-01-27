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
    insert_1_op = b.insert_many(1, keys[0:2], values_1[0:2])
    insert_2_op = b.insert_many(1, keys[2:], values_1[2:])
    cancel_op = b.close(cancel_pending_enqueues=True)
    fail_insert_op = b.insert_many(0, ["f"], [60.0])
    take_t = b.take_many(2)
    take_too_many_t = b.take_many(3)

    self.assertEqual(self.evaluate(size_t), [0])
    insert_0_op.run()
    insert_1_op.run()
    self.assertEqual(self.evaluate(size_t), [2])
    self.assertEqual(self.evaluate(incomplete_t), [1])
    cancel_op.run()

    # This op should fail because the queue is closed.
    with self.assertRaisesOpError("is closed"):
        fail_insert_op.run()

    # This op should fail because the queue is canceled.
    with self.assertRaisesOpError("is closed"):
        insert_2_op.run()

    # This op should fail because we requested more elements than are
    # available in incomplete + ready queue.
    with self.assertRaisesOpError(r"is closed and has insufficient elements "
                                  r"\(requested 3, total size 2\)"):
        sess.run(take_too_many_t[0])  # Sufficient to request just the indices

    # This op should succeed because there are still completed elements
    # to process.
    indices_val, keys_val, values_0_val, values_1_val = sess.run(
        [take_t[0], take_t[1], take_t[2][0], take_t[2][1]])
    self.assertAllEqual(indices_val, [-2**63] * 2)
    for k, v0, v1 in zip(keys[0:2], values_0[0:2], values_1[0:2]):
        idx = keys_val.tolist().index(k)
        self.assertEqual(values_0_val[idx], v0)
        self.assertEqual(values_1_val[idx], v1)

    # This op should fail because there are no more completed elements and
    # the queue is closed.
    with self.assertRaisesOpError("is closed and has insufficient elements"):
        sess.run(take_t[0])
