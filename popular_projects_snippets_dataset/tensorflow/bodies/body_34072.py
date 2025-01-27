# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/barrier_ops_test.py
with self.cached_session() as sess:
    b = data_flow_ops.Barrier(
        (dtypes.float32, dtypes.float32), shapes=((), ()), name="B")
    size_t = b.ready_size()
    size_i = b.incomplete_size()
    keys = [b"a", b"b", b"c", b"d"]
    values_0 = [10.0, 20.0, 30.0, 40.0]
    values_1 = [100.0, 200.0, 300.0, 400.0]
    insert_0_op = b.insert_many(0, keys, values_0)
    # Split adding of the second component into two independent operations.
    # After insert_1_1_op, we'll have two ready elements in the barrier,
    # 2 will still be incomplete.
    insert_1_1_op = b.insert_many(1, keys[0:2], values_1[0:2])  # add "a", "b"
    insert_1_2_op = b.insert_many(1, keys[2:3], values_1[2:3])  # add "c"
    insert_1_3_op = b.insert_many(1, keys[3:], values_1[3:])  # add "d"
    insert_empty_op = b.insert_many(0, [], [])
    close_op = b.close()
    close_op_final = b.close(cancel_pending_enqueues=True)
    index_t, key_t, value_list_t = b.take_many(3, allow_small_batch=True)
    insert_0_op.run()
    insert_1_1_op.run()
    close_op.run()
    # Now we have a closed barrier with 2 ready elements. Running take_t
    # should return a reduced batch with 2 elements only.
    self.assertEqual(self.evaluate(size_i),
                     [2])  # assert that incomplete size = 2
    self.assertEqual(self.evaluate(size_t), [2])  # assert that ready size = 2
    _, keys_val, values_0_val, values_1_val = sess.run(
        [index_t, key_t, value_list_t[0], value_list_t[1]])
    # Check that correct values have been returned.
    for k, v0, v1 in zip(keys[0:2], values_0[0:2], values_1[0:2]):
        idx = keys_val.tolist().index(k)
        self.assertEqual(values_0_val[idx], v0)
        self.assertEqual(values_1_val[idx], v1)

    # The next insert completes the element with key "c". The next take_t
    # should return a batch with just 1 element.
    insert_1_2_op.run()
    self.assertEqual(self.evaluate(size_i),
                     [1])  # assert that incomplete size = 1
    self.assertEqual(self.evaluate(size_t), [1])  # assert that ready size = 1
    _, keys_val, values_0_val, values_1_val = sess.run(
        [index_t, key_t, value_list_t[0], value_list_t[1]])
    # Check that correct values have been returned.
    for k, v0, v1 in zip(keys[2:3], values_0[2:3], values_1[2:3]):
        idx = keys_val.tolist().index(k)
        self.assertEqual(values_0_val[idx], v0)
        self.assertEqual(values_1_val[idx], v1)

    # Adding nothing ought to work, even if the barrier is closed.
    insert_empty_op.run()

    # currently keys "a" and "b" are not in the barrier, adding them
    # again after it has been closed, ought to cause failure.
    with self.assertRaisesOpError("is closed"):
        insert_1_1_op.run()
    close_op_final.run()

    # These ops should fail because the barrier has now been closed with
    # cancel_pending_enqueues = True.
    with self.assertRaisesOpError("is closed"):
        insert_empty_op.run()
    with self.assertRaisesOpError("is closed"):
        insert_1_3_op.run()
