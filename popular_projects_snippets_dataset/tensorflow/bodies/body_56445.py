# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
# Produce GraphDef containing while loop.
graph = ops.Graph()
with graph.as_default():
    r = control_flow_ops.while_loop(lambda i: i < 10, lambda i: i + 1, [0])
graph_def = graph.as_graph_def()

# Import the GraphDef inside a cond and make sure it runs.
with ops.Graph().as_default():

    def ImportFn():
        exit(importer.import_graph_def(graph_def, return_elements=[r.name])[0])

    pred = array_ops.placeholder(dtypes.bool)
    out = control_flow_ops.cond(pred, ImportFn,
                                lambda: constant_op.constant(1))
    with self.cached_session() as sess:
        self.assertEqual(sess.run(out, {pred: True}), 10)
        self.assertEqual(sess.run(out, {pred: False}), 1)
