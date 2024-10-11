# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph_test.py
with ops.Graph().as_default():
    variables.Variable(0, name="v")
    meta_graph_def, _ = meta_graph.export_scoped_meta_graph()
with ops.Graph().as_default():
    for suffix in ["", "_1"]:
        imported_variables = meta_graph.import_scoped_meta_graph(
            meta_graph_def, import_scope="s")
        self.assertEqual(len(imported_variables), 1)
        self.assertEqual(list(imported_variables.keys())[0], "v:0")
        self.assertEqual(list(imported_variables.values())[0].name,
                         "s" + suffix + "/v:0")
