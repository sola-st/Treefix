# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/loader_test.py
# Force test to run in graph mode.
# The SavedModelLoader.restore_variables method is a v1-only API requiring a
# session to work.
with ops.Graph().as_default():
    self.export_graph_with_main_op(builder_cls)
    loader = loader_impl.SavedModelLoader(SAVED_MODEL_WITH_MAIN_OP)
    with self.session() as sess:
        x = variables.VariableV1(0, name="x")
        y = variables.VariableV1(0, name="y")
        z = x * y

        self.evaluate(variables.global_variables_initializer())

        # There are variables to restore, so a saver must be created.
        with self.assertRaises(ValueError):
            loader.restore_variables(sess, None)

        loader.restore_variables(sess, tf_saver.Saver())
        self.assertEqual(55, self.evaluate(z))
