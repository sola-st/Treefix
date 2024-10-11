# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/loader_test.py
# Force test to run in graph mode.
# The SavedModelLoader.restore_variables and SavedModelLoader.run_init_ops
# methods are v1-only APIs that require a session to work.
with ops.Graph().as_default():
    self.export_graph_with_main_op(builder_cls)
    loader = loader_impl.SavedModelLoader(SAVED_MODEL_WITH_MAIN_OP)
    with self.session(graph=ops.Graph()) as sess:
        saver, _ = loader.load_graph(
            sess.graph, ["foo_graph"], import_scope="baz")

        # The default saver should not work when the import scope is set.
        with self.assertRaises(errors.NotFoundError):
            loader.restore_variables(sess, tf_saver.Saver())

        loader.restore_variables(sess, saver)

        if builder_cls == saved_model_builder._SavedModelBuilder:
            with self.assertRaises(errors.NotFoundError):
                loader.run_init_ops(sess, ["foo_graph"])
            loader.run_init_ops(sess, ["foo_graph"], import_scope="baz")
        else:
            loader.run_init_ops(sess, ["foo_graph"])

        self.assertEqual(5, sess.run(_tensor_name("baz/x")))
        self.assertEqual(7, sess.run(_tensor_name("baz/y")))

    # Test combined load function.
    loader = loader_impl.SavedModelLoader(SAVED_MODEL_WITH_MAIN_OP)
    with self.session(graph=ops.Graph()) as sess:
        loader.load(sess, ["foo_graph"], import_scope="baa")
        self.assertEqual(5, sess.run(_tensor_name("baa/x")))
        self.assertEqual(7, sess.run(_tensor_name("baa/y")))
