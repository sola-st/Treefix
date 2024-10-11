# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
if is_anonymous and not tf2.enabled():
    self.skipTest(SKIP_ANONYMOUS_IN_TF1_REASON)
save_dir = os.path.join(self.get_temp_dir(), "save_restore")
save_path = os.path.join(tempfile.mkdtemp(prefix=save_dir), "hash")

with self.session(graph=ops.Graph()) as sess:
    v0 = variables.Variable(10.0, name="v0")
    v1 = variables.Variable(20.0, name="v1")

    default_val = -1
    keys = constant_op.constant(["b", "c", "d"], dtypes.string)
    values = constant_op.constant([0, 1, 2], dtypes.int64)
    table = lookup_ops.MutableHashTable(
        dtypes.string,
        dtypes.int64,
        default_val,
        name="t1",
        checkpoint=True,
        experimental_is_anonymous=is_anonymous)

    save = saver.Saver([table])
    self.evaluate(variables.global_variables_initializer())

    # Check that the parameter nodes have been initialized.
    self.assertEqual(10.0, self.evaluate(v0))
    self.assertEqual(20.0, self.evaluate(v1))

    self.assertAllEqual(0, self.evaluate(table.size()))
    self.evaluate(table.insert(keys, values))
    self.assertAllEqual(3, self.evaluate(table.size()))

    val = save.save(sess, save_path)
    self.assertIsInstance(val, str)
    self.assertEqual(save_path, val)

with self.session(graph=ops.Graph()) as sess:
    default_val = -1
    table = lookup_ops.MutableHashTable(
        dtypes.string,
        dtypes.int64,
        default_val,
        name="t1",
        checkpoint=True,
        experimental_is_anonymous=is_anonymous)
    self.evaluate(
        table.insert(
            constant_op.constant(["a", "c"], dtypes.string),
            constant_op.constant([12, 24], dtypes.int64)))
    self.assertAllEqual(2, self.evaluate(table.size()))

    save = saver.Saver([table])

    # Restore the saved values in the parameter nodes.
    save.restore(sess, save_path)
    # Check that the parameter nodes have been restored.

    self.assertAllEqual(3, self.evaluate(table.size()))

    input_string = constant_op.constant(["a", "b", "c", "d", "e"],
                                        dtypes.string)
    output = table.lookup(input_string)
    self.assertAllEqual([-1, 0, 1, 2, -1], self.evaluate(output))
