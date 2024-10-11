# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/loader_test.py
# Force test to run in graph mode.
# The SavedModelLoader.load method is a v1-only API that requires a session
# to work.
with ops.Graph().as_default():
    self.export_simple_graph(builder_cls)
    loader = loader_impl.SavedModelLoader(SIMPLE_ADD_SAVED_MODEL)
    with self.session(graph=ops.Graph()) as sess:
        loader.load(sess, ["foo_graph"])
        self.assertEqual(5, sess.run(_tensor_name("x")))
        self.assertEqual(11, sess.run(_tensor_name("y")))

    self.export_graph_with_main_op(builder_cls)
    loader2 = loader_impl.SavedModelLoader(SAVED_MODEL_WITH_MAIN_OP)
    with self.session(graph=ops.Graph()) as sess:
        loader2.load(sess, ["foo_graph"])
        self.assertEqual(5, sess.run(_tensor_name("x")))
        self.assertEqual(7, sess.run(_tensor_name("y")))
