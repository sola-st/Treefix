# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/saved_model_test.py
export_dir = self._get_export_dir("test_no_custom_saver")
builder = saved_model_builder._SavedModelBuilder(export_dir)

with ops.Graph().as_default() as graph:
    with self.session(graph=ops.Graph()) as sess:
        variables.VariableV1(1, name="v1")
        self.evaluate(variables.global_variables_initializer())
        training.Saver(name="my_saver")
        builder.add_meta_graph_and_variables(sess, ["tag"])

    # Save the SavedModel to disk.
    builder.save()

    with self.session(graph=graph) as sess:
        saved_graph = loader.load(sess, ["tag"], export_dir)
        graph_ops = [x.name for x in graph.get_operations()]
        self.assertTrue("my_saver/restore_all" in graph_ops)
        self.assertTrue("save/restore_all" in graph_ops)
        self.assertEqual(
            saved_graph.saver_def.restore_op_name, "save/restore_all")
