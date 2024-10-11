# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
if is_anonymous and not tf2.enabled():
    self.skipTest(SKIP_ANONYMOUS_IN_TF1_REASON)
save_dir = os.path.join(self.get_temp_dir(), "save_restore")
save_path = os.path.join(tempfile.mkdtemp(prefix=save_dir), "hash")

with self.session(graph=ops.Graph()) as sess:
    default_value = -1
    empty_key = 0
    deleted_key = -1
    keys = constant_op.constant([11, 12, 13, 14], dtypes.int64)
    values = constant_op.constant([0, 1, 2, 3], dtypes.int64)
    table = lookup_ops.DenseHashTable(
        dtypes.int64,
        dtypes.int64,
        default_value=default_value,
        empty_key=empty_key,
        deleted_key=deleted_key,
        name="t1",
        checkpoint=True,
        initial_num_buckets=32,
        experimental_is_anonymous=is_anonymous)

    save = saver.Saver()

    self.assertAllEqual(0, table.size())
    table.insert(keys, values).run()
    self.assertAllEqual(4, table.size())
    self.assertAllEqual(32, len(table.export()[0].eval()))

    keys2 = constant_op.constant([12, 15], dtypes.int64)
    table.remove(keys2).run()
    self.assertAllEqual(3, table.size())
    self.assertAllEqual(32, len(table.export()[0].eval()))

    val = save.save(sess, save_path)
    self.assertIsInstance(val, str)
    self.assertEqual(save_path, val)

with self.session(graph=ops.Graph()) as sess:
    table = lookup_ops.DenseHashTable(
        dtypes.int64,
        dtypes.int64,
        default_value=default_value,
        empty_key=empty_key,
        deleted_key=deleted_key,
        name="t1",
        checkpoint=True,
        initial_num_buckets=64,
        experimental_is_anonymous=is_anonymous)
    table.insert(
        constant_op.constant([11, 14], dtypes.int64),
        constant_op.constant([12, 24], dtypes.int64)).run()
    self.assertAllEqual(2, table.size())
    self.assertAllEqual(64, len(table.export()[0].eval()))

    save = saver.Saver()

    # Restore the saved values in the parameter nodes.
    save.restore(sess, save_path)

    self.assertAllEqual(3, table.size())
    self.assertAllEqual(32, len(table.export()[0].eval()))

    input_string = constant_op.constant([10, 11, 12, 13, 14], dtypes.int64)
    output = table.lookup(input_string)
    self.assertAllEqual([-1, 0, -1, 2, 3], output)
