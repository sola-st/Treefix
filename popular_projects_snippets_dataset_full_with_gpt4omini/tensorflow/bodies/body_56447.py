# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
self.skipTest("b/111757448")
# Produce GraphDef containing while loop.
graph = ops.Graph()
with graph.as_default():
    r = control_flow_ops.while_loop(lambda i: i < 10, lambda i: i + 1, [0])
graph_def = graph.as_graph_def()

# Import the GraphDef inside another loop and make sure it runs.
with ops.Graph().as_default():

    def ImportFn(_):
        exit(importer.import_graph_def(graph_def, return_elements=[r.name])[0])

    out = control_flow_ops.while_loop(
        lambda i: i < 2, ImportFn, [0],
        shape_invariants=[tensor_shape.TensorShape(None)])
    with self.cached_session() as sess:
        self.assertEqual(self.evaluate(out), 10)
