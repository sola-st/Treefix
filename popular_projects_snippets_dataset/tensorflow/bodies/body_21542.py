# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
test_dir = self._get_test_dir("slice_saver")
filename = os.path.join(test_dir, "metafile")
with self.cached_session():
    v1 = variables.VariableV1([20.0], name="v1")
    v2 = variables.VariableV1([20.0], name="v2")
    v2._set_save_slice_info(
        variables.Variable.SaveSliceInfo("v1", [1], [0], [1]))

    # The names are different and will work.
    slice_saver = saver_module.Saver({"first": v1, "second": v2})
    self.evaluate(variables.global_variables_initializer())
    # Exports to meta_graph
    meta_graph_def = slice_saver.export_meta_graph(filename)

with ops_lib.Graph().as_default():
    # Restores from MetaGraphDef.
    new_saver = saver_module.import_meta_graph(filename)
    self.assertIsNotNone(new_saver)
    # Generates a new MetaGraphDef.
    new_meta_graph_def = new_saver.export_meta_graph()
    # It should be the same as the original.
    test_util.assert_meta_graph_protos_equal(self, meta_graph_def,
                                             new_meta_graph_def)
