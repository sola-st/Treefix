# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py
root = autotrackable.AutoTrackable()
root.uninitialized_variable = resource_variable_ops.UninitializedVariable(
    name="uninitialized_variable", dtype=dtypes.float32)
root.initialized_variable = variables.Variable(
    1.0, name="initialized_variable")

# TODO(b/149594077): Python loading does not work now partly because it
# shouldn't, as the public API and semantics of uninitialized variables
# are not properly defined, and officially supporting loading would end up
# defining semantics "by usage." We should only allow loading once the API
# is made official.
export_dir = os.path.join(self.get_temp_dir(), "saved_model")
save.save(root, export_dir)
with self.assertRaisesRegex(FileNotFoundError,
                            "Key uninitialized_variable"):
    load.load(export_dir)
with ops.Graph().as_default(), session_lib.Session() as session:
    # The final ValueError here (with "no variables to save") is confusing,
    # but errors upstream give the user the correct information (a
    # NotFoundError stating that the uninitalized_variable was not found in
    # the checkpoint).
    with self.assertRaises(ValueError):
        loader.load(session, [tag_constants.SERVING], export_dir)
