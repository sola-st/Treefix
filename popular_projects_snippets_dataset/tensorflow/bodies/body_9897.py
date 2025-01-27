# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_utils_test.py
saved_model_dir = os.path.join(test.get_temp_dir(), "test_invalid_tags")
builder = saved_model_builder.SavedModelBuilder(saved_model_dir)
# Force test to run in graph mode since SavedModelBuilder.save requires a
# session to work.
with ops.Graph().as_default() as g:
    with self.session(graph=g) as sess:
        self._init_and_validate_variable(sess, "v", 42)
        builder.add_meta_graph_and_variables(sess, ["a", "b"])
    builder.save()

# Sanity check
saved_model_utils.get_meta_graph_def(saved_model_dir, "a,b")

with self.assertRaisesRegex(RuntimeError, "associated with tag-set"):
    saved_model_utils.get_meta_graph_def(saved_model_dir, "c,d")
