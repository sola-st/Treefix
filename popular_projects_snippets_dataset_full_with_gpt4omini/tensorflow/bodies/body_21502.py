# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
# ParseURI functions don't work on Windows yet.
# TODO(jhseu): Remove this check when it works.
if os.name == "nt":
    self.skipTest("Local URI support doesn't work on Windows")
save_path = "file://" + os.path.join(self.get_temp_dir(), "uri")

# Build a graph with 2 parameter nodes, and Save and
# Restore nodes for them.
v0 = variables.VariableV1(10.0, name="v0")
v1 = variables.VariableV1(20.0, name="v1")
save = saver_module.Saver({"v0": v0, "v1": v1}, restore_sequentially=True)
init_all_op = variables.global_variables_initializer()

with self.cached_session() as sess:
    # Initialize all variables
    self.evaluate(init_all_op)

    # Check that the parameter nodes have been initialized.
    self.assertEqual(10.0, self.evaluate(v0))
    self.assertEqual(20.0, self.evaluate(v1))
    save.save(sess, save_path)
