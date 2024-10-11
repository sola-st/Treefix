# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/saved_model_test.py
export_dir = self._get_export_dir("test_sequence")
builder = saved_model_builder._SavedModelBuilder(export_dir)

with ops.Graph().as_default():
    # Expect an assertion error since add_meta_graph_and_variables() should be
    # invoked before any add_meta_graph() calls.
    with self.session(graph=ops.Graph()) as sess:
        self.assertRaises(AssertionError, builder.add_meta_graph, ["foo"])

    # Expect an assertion error for multiple calls of
    # add_meta_graph_and_variables() since weights should be saved exactly
    # once.
    with self.session(graph=ops.Graph()) as sess:
        self._init_and_validate_variable(sess, "v", 42)
        builder.add_meta_graph_and_variables(sess, ["bar"])
        self.assertRaises(AssertionError, builder.add_meta_graph_and_variables,
                          sess, ["baz"])
