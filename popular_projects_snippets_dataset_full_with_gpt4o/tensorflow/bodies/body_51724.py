# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/loader_test.py
"""Test that SavedModel runs saver when there appear to be no variables.

    When no variables are detected, this may mean that the variables were saved
    to different collections, or the collections weren't saved to the
    SavedModel. If the SavedModel MetaGraphDef contains a saver, it should still
    run in either of these cases.

    Args:
      builder_cls: SavedModelBuilder or _SavedModelBuilder class
    """
# Force test to run in graph mode.
# The SavedModelBuilder.add_meta_graph_and_variables and
# SavedModelLoader.load methods are v1-only APIs that require a session to
# work.
with ops.Graph().as_default():
    path = _get_export_dir("no_variable_saved_model")
    with session.Session(graph=ops.Graph()) as sess:
        x = variables.VariableV1(
            5, name="x", collections=["not_global_variable"])
        y = variables.VariableV1(
            11, name="y", collections=["not_global_variable"])
        self.assertFalse(variables._all_saveable_objects())
        z = x + y
        self.evaluate(variables.variables_initializer([x, y]))

        foo_sig_def = signature_def_utils.build_signature_def(
            {"foo_input": utils.build_tensor_info(x)},
            {"foo_output": utils.build_tensor_info(z)})

        builder = saved_model_builder.SavedModelBuilder(path)
        builder.add_meta_graph_and_variables(
            sess, ["foo_graph"], {"foo": foo_sig_def},
            saver=tf_saver.Saver([x, y]))
        builder.save()

    loader = loader_impl.SavedModelLoader(path)
    with self.session(graph=ops.Graph()) as sess:
        saver, _ = loader.load_graph(sess.graph, ["foo_graph"])
        self.assertFalse(variables._all_saveable_objects())
        self.assertIsNotNone(saver)

    with self.session(graph=ops.Graph()) as sess:
        loader.load(sess, ["foo_graph"])
        self.assertEqual(5, sess.run(_tensor_name("x")))
        self.assertEqual(11, sess.run(_tensor_name("y")))
