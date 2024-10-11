# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/loader_test.py
# Force test to run in graph mode.
# The SavedModelLoader.restore_variables and SavedModelLoader.run_init_ops
# methods are v1-only APIs that require a session to work.
with ops.Graph().as_default():
    self.export_graph_with_main_op(builder_cls)
    loader = loader_impl.SavedModelLoader(SAVED_MODEL_WITH_MAIN_OP)
    graph = ops.Graph()
    saver, _ = loader.load_graph(graph, ["foo_graph"])
    with self.session(graph=graph) as sess:
        loader.restore_variables(sess, saver)
        self.assertEqual(5, sess.run(_tensor_name("x")))
        self.assertEqual(11, sess.run(_tensor_name("y")))

        loader.run_init_ops(sess, ["foo_graph"])
        self.assertEqual(5, sess.run(_tensor_name("x")))
        self.assertEqual(7, sess.run(_tensor_name("y")))
