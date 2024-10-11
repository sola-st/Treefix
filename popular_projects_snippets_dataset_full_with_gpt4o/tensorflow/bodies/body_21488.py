# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
save_path = os.path.join(self.get_temp_dir(), "basics_with_list")

with self.session(graph=ops_lib.Graph()) as sess:
    # Build a graph with 2 parameter nodes, and Save and
    # Restore nodes for them.
    v0 = variables.VariableV1(10.0, name="v0")
    v1 = variables.VariableV1(20.0, name="v1")
    v2 = saver_test_utils.CheckpointedOp(name="v2")
    v2_init = v2.insert("k1", 30.0)
    save = saver_module.Saver([v0, v1, v2.saveable])
    self.evaluate(variables.global_variables_initializer())
    v2_init.run()

    # Check that the parameter nodes have been initialized.
    self.assertEqual(10.0, self.evaluate(v0))
    self.assertEqual(20.0, self.evaluate(v1))
    self.assertEqual(b"k1", self.evaluate(v2.keys()))
    self.assertEqual(30.0, self.evaluate(v2.values()))

    # Save the initialized values in the file at "save_path"
    val = save.save(sess, save_path)
    self.assertIsInstance(val, str)
    self.assertEqual(save_path, val)

# Start a second session.  In that session the variables
# have not been initialized either.
with self.session(graph=ops_lib.Graph()) as sess:
    v0 = variables.VariableV1(-1.0, name="v0")
    v1 = variables.VariableV1(-1.0, name="v1")
    v2 = saver_test_utils.CheckpointedOp(name="v2")
    save = saver_module.Saver([v0, v1, v2.saveable])

    with self.assertRaisesWithPredicateMatch(
        errors_impl.OpError, lambda e: "uninitialized value v0" in e.message):
        self.evaluate(v0)
    with self.assertRaisesWithPredicateMatch(
        errors_impl.OpError, lambda e: "uninitialized value v1" in e.message):
        self.evaluate(v1)
    self.assertEqual(0, len(self.evaluate(v2.keys())))
    self.assertEqual(0, len(self.evaluate(v2.values())))

    # Restore the saved values in the parameter nodes.
    save.restore(sess, save_path)
    # Check that the parameter nodes have been restored.
    self.assertEqual(10.0, self.evaluate(v0))
    self.assertEqual(20.0, self.evaluate(v1))
    self.assertEqual(b"k1", self.evaluate(v2.keys()))
    self.assertEqual(30.0, self.evaluate(v2.values()))

# Build another graph with 2 nodes, initialized
# differently, and a Restore node for them.
with self.session(graph=ops_lib.Graph()) as sess:
    v0_2 = variables.VariableV1(1000.0, name="v0")
    v1_2 = variables.VariableV1(2000.0, name="v1")
    v2_2 = saver_test_utils.CheckpointedOp(name="v2")
    save2 = saver_module.Saver([v0_2, v1_2, v2_2.saveable])
    v2_2.insert("k1000", 3000.0).run()
    self.evaluate(variables.global_variables_initializer())

    # Check that the parameter nodes have been initialized.
    self.assertEqual(1000.0, self.evaluate(v0_2))
    self.assertEqual(2000.0, self.evaluate(v1_2))
    self.assertEqual(b"k1000", self.evaluate(v2_2.keys()))
    self.assertEqual(3000.0, self.evaluate(v2_2.values()))
    # Restore the values saved earlier in the parameter nodes.
    save2.restore(sess, save_path)
    # Check that the parameter nodes have been restored.
    self.assertEqual(10.0, self.evaluate(v0_2))
    self.assertEqual(20.0, self.evaluate(v1_2))
    self.assertEqual(b"k1", self.evaluate(v2_2.keys()))
    self.assertEqual(30.0, self.evaluate(v2_2.values()))
