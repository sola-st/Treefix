# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/saved_model_test.py
export_dir = self._get_export_dir("test_multiple_custom_savers")
builder = saved_model_builder._SavedModelBuilder(export_dir)

with ops.Graph().as_default():
    with self.session(graph=ops.Graph()) as sess:
        variables.VariableV1(1, name="v1")
        self.evaluate(variables.global_variables_initializer())
        builder.add_meta_graph_and_variables(sess, ["tag_0"])

        saver_1 = training.Saver()
        builder.add_meta_graph(["tag_1"], saver=saver_1)

        saver_2 = training.Saver()
        builder.add_meta_graph(["tag_2"], saver=saver_2)

    # Save the SavedModel to disk.
    builder.save()

def _validate_custom_saver(tag_name, saver_name):
    with ops.Graph().as_default() as graph:
        with self.session(graph=graph) as sess:
            saved_graph = loader.load(sess, [tag_name], export_dir)
            self.assertEqual(
                saved_graph.saver_def.restore_op_name,
                saver_name)

_validate_custom_saver("tag_0", "save/restore_all")
_validate_custom_saver("tag_1", "save_1/restore_all")
_validate_custom_saver("tag_2", "save_2/restore_all")
