# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph_test.py
graph = ops.Graph()
with graph.as_default():
    variables.Variable(initial_value=1.0, trainable=True, name="myvar")
meta_graph_def, _ = meta_graph.export_scoped_meta_graph(graph=graph)

graph = ops.Graph()
with graph.as_default():
    with ops.name_scope("foo"):
        imported_variables = meta_graph.import_scoped_meta_graph(
            meta_graph_def, import_scope="bar")
        self.assertEqual(len(imported_variables), 1)
        self.assertEqual(list(imported_variables.values())[0].name,
                         "foo/bar/myvar:0")
