# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
# Produce GraphDef containing while loop.
graph = ops.Graph()
with graph.as_default():
    r = control_flow_ops.while_loop(lambda i: i < 10, lambda i: i + 1, [0])
    # Add an op that consumes the while loop output.
    math_ops.add(r, 1)
graph_def = graph.as_graph_def()

# Import the GraphDef and make sure it runs.
with ops.Graph().as_default():
    imported_r, = importer.import_graph_def(graph_def,
                                            return_elements=[r.name])
    self.assertEqual(imported_r.name, "import/" + r.name)
    with self.cached_session() as sess:
        self.assertEqual(self.evaluate(imported_r), 10)
