# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/saved_model_test.py
export_dir = self._get_export_dir("test_astext")
builder = saved_model_builder._SavedModelBuilder(export_dir)

with ops.Graph().as_default():
    # Graph with a single variable. SavedModel invoked to:
    # - add with weights.
    with self.session(graph=ops.Graph()) as sess:
        self._init_and_validate_variable(sess, "v", 42)
        builder.add_meta_graph_and_variables(sess, ["foo"])

    # Graph with the same single variable. SavedModel invoked to:
    # - simply add the model (weights are not updated).
    with self.session(graph=ops.Graph()) as sess:
        self._init_and_validate_variable(sess, "v", 43)
        builder.add_meta_graph(["bar"])

    # Save the SavedModel to disk in text format.
    builder.save(as_text=True)

    # Restore the graph with tag "foo", whose variables were saved.
    with self.session(graph=ops.Graph()) as sess:
        loader.load(sess, ["foo"], export_dir)
        self.assertEqual(
            42,
            self._eval(ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)[0]))

    # Restore the graph with tag "bar", whose variables were not saved.
    with self.session(graph=ops.Graph()) as sess:
        loader.load(sess, ["bar"], export_dir)
        self.assertEqual(
            42,
            self._eval(ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)[0]))
