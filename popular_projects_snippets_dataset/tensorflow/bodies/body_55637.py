# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph_test.py
with ops.Graph().as_default() as graph1:
    v = variables.Variable(3.0)
    # A single instance of Variable is shared among the collections:
    global_vars = graph1.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)
    trainable_vars = graph1.get_collection(ops.GraphKeys.TRAINABLE_VARIABLES)
    self.assertEqual(len(global_vars), 1)
    self.assertEqual(len(trainable_vars), 1)
    self.assertIs(global_vars[0], trainable_vars[0])
    self.assertIs(v, global_vars[0])

orig_meta_graph, _ = meta_graph.export_scoped_meta_graph(graph=graph1)
del graph1  # To avoid accidental references in code involving graph2.

with ops.Graph().as_default() as graph2:
    meta_graph.import_scoped_meta_graph(orig_meta_graph)
    global_vars = graph2.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)
    trainable_vars = graph2.get_collection(ops.GraphKeys.TRAINABLE_VARIABLES)
    self.assertEqual(len(global_vars), 1)
    self.assertEqual(len(trainable_vars), 1)
    # A single instance of Variable is shared among the collections:
    self.assertIs(global_vars[0], trainable_vars[0])
