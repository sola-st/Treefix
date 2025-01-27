# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/saved_model_test.py
export_dir = self._get_export_dir("test_verify_session_graph_usage")
builder = saved_model_builder._SavedModelBuilder(export_dir)

with ops.Graph().as_default():
    with self.session(graph=ops.Graph()) as sess:
        self._init_and_validate_variable(sess, "v", 42)
        builder.add_meta_graph_and_variables(sess, [tag_constants.TRAINING])

    # Save the SavedModel to disk.
    builder.save()

    # Build a session and supply it to the load operation.
    sess = session.Session(graph=ops.Graph())
    loader.load(sess, [tag_constants.TRAINING], export_dir)

    # Check the variable within the scope of the session and its graph.
    with sess:
        self.assertEqual(
            42,
            self._eval(ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)[0]))
